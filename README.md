# Spy Cat Agency (SCA) Management System

A Django REST Framework application for managing spy cats, missions, and targets.

## Setup

### Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver
```

## API Testing Guide

Base URL: `http://localhost:8000/api`

---

## Spy Cats Endpoints

[Postman collection link](https://.postman.co/workspace/My-Workspace~bc9cf8fa-f883-413d-8e00-3a7f51e7ebd5/collection/30093965-59d16deb-04fa-4005-88db-d77bb3326774?action=share&creator=30093965)

I have also attached file 'SCA_API_Collection.postman_collection.json'. You can import it to Postman and test the app if the collection link doesn't work..

### 1. Create a Spy Cat

**Endpoint:** `POST /api/cats/`

**Valid Breed Example:**
```bash
curl -X POST http://localhost:8000/api/cats/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Agent Whiskers",
    "years_of_experience": 5,
    "breed": "Siamese",
    "salary": 50000.00
  }'
```

**Response:**
```json
{
  "id": 1,
  "name": "Agent Whiskers",
  "years_of_experience": 5,
  "breed": "Siamese",
  "salary": "50000.00",
  "created_at": "2024-11-19T20:00:00Z",
  "updated_at": "2024-11-19T20:00:00Z"
}
```

**Invalid Breed Example:**
```bash
curl -X POST http://localhost:8000/api/cats/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Agent Fluffy",
    "years_of_experience": 3,
    "breed": "InvalidBreed123",
    "salary": 45000.00
  }'
```

**Error Response:**
```json
{
  "breed": [
    "Breed 'InvalidBreed123' is not a valid cat breed."
  ]
}
```

**More Valid Breeds to Test:**
```bash
# Persian
curl -X POST http://localhost:8000/api/cats/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Agent Shadow",
    "years_of_experience": 7,
    "breed": "Persian",
    "salary": 60000.00
  }'

# Maine Coon
curl -X POST http://localhost:8000/api/cats/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Agent Tiger",
    "years_of_experience": 4,
    "breed": "Maine Coon",
    "salary": 55000.00
  }'

# British Shorthair
curl -X POST http://localhost:8000/api/cats/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Agent Mittens",
    "years_of_experience": 6,
    "breed": "British Shorthair",
    "salary": 52000.00
  }'
```

**More Invalid Breeds to Test:**
```bash
# Completely fake breed
curl -X POST http://localhost:8000/api/cats/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Agent Test",
    "years_of_experience": 2,
    "breed": "SuperCat",
    "salary": 40000.00
  }'

# Dog breed (should fail)
curl -X POST http://localhost:8000/api/cats/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Agent Spot",
    "years_of_experience": 3,
    "breed": "Golden Retriever",
    "salary": 45000.00
  }'

# Typo in breed name
curl -X POST http://localhost:8000/api/cats/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Agent Fuzzy",
    "years_of_experience": 5,
    "breed": "Siameze",
    "salary": 48000.00
  }'
```

### 2. List All Spy Cats

**Endpoint:** `GET /api/cats/`

```bash
curl -X GET http://localhost:8000/api/cats/
```

**Response:**
```json
{
  "count": 4,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Agent Whiskers",
      "years_of_experience": 5,
      "breed": "Siamese",
      "salary": "50000.00",
      "created_at": "2024-11-19T20:00:00Z",
      "updated_at": "2024-11-19T20:00:00Z"
    },
    ...
  ]
}
```

### 3. Get a Single Spy Cat

**Endpoint:** `GET /api/cats/{id}/`

```bash
curl -X GET http://localhost:8000/api/cats/1/
```

**Response:**
```json
{
  "id": 1,
  "name": "Agent Whiskers",
  "years_of_experience": 5,
  "breed": "Siamese",
  "salary": "50000.00",
  "created_at": "2024-11-19T20:00:00Z",
  "updated_at": "2024-11-19T20:00:00Z"
}
```

### 4. Update Spy Cat Information (Salary)

**Endpoint:** `PATCH /api/cats/{id}/`

```bash
curl -X PATCH http://localhost:8000/api/cats/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "salary": 55000.00
  }'
```

**Response:**
```json
{
  "salary": "55000.00"
}
```

### 5. Remove Spy Cat from System

**Endpoint:** `DELETE /api/cats/{id}/`

```bash
curl -X DELETE http://localhost:8000/api/cats/4/
```

**Response:** `204 No Content`

---

## Missions & Targets Endpoints

### 1. Create a Mission with Targets (Single Request)

**Endpoint:** `POST /api/missions/`

**Example with 1 Target (Minimum):**
```bash
curl -X POST http://localhost:8000/api/missions/ \
  -H "Content-Type: application/json" \
  -d '{
    "targets": [
      {
        "name": "Dr. Evil",
        "country": "Russia",
        "notes": "High priority target"
      }
    ]
  }'
```

**Example with 3 Targets (Maximum):**
```bash
curl -X POST http://localhost:8000/api/missions/ \
  -H "Content-Type: application/json" \
  -d '{
    "targets": [
      {
        "name": "Target Alpha",
        "country": "USA",
        "notes": "Gather intelligence on location"
      },
      {
        "name": "Target Beta",
        "country": "UK",
        "notes": "Monitor communications"
      },
      {
        "name": "Target Gamma",
        "country": "France",
        "notes": "Track movements"
      }
    ]
  }'
```

**Response:**
```json
{
  "id": 1,
  "cat": null,
  "cat_name": null,
  "is_complete": false,
  "targets": [
    {
      "id": 1,
      "name": "Target Alpha",
      "country": "USA",
      "notes": "Gather intelligence on location",
      "is_complete": false,
      "created_at": "2024-11-19T20:00:00Z",
      "updated_at": "2024-11-19T20:00:00Z"
    },
    ...
  ],
  "created_at": "2024-11-19T20:00:00Z",
  "updated_at": "2024-11-19T20:00:00Z"
}
```

**Invalid: 0 Targets (Should Fail):**
```bash
curl -X POST http://localhost:8000/api/missions/ \
  -H "Content-Type: application/json" \
  -d '{
    "targets": []
  }'
```

**Error Response:**
```json
{
  "targets": [
    "A mission must have between 1 and 3 targets."
  ]
}
```

**Invalid: 4 Targets (Should Fail):**
```bash
curl -X POST http://localhost:8000/api/missions/ \
  -H "Content-Type: application/json" \
  -d '{
    "targets": [
      {"name": "Target 1", "country": "USA", "notes": ""},
      {"name": "Target 2", "country": "UK", "notes": ""},
      {"name": "Target 3", "country": "France", "notes": ""},
      {"name": "Target 4", "country": "Germany", "notes": ""}
    ]
  }'
```

**Error Response:**
```json
{
  "targets": [
    "A mission must have between 1 and 3 targets."
  ]
}
```

### 2. Assign a Cat to a Mission

**Endpoint:** `PATCH /api/missions/{id}/assign_cat/`

```bash
curl -X PATCH http://localhost:8000/api/missions/1/assign_cat/ \
  -H "Content-Type: application/json" \
  -d '{
    "cat_id": 1
  }'
```

**Response:**
```json
{
  "id": 1,
  "cat": 1,
  "cat_name": "Agent Whiskers",
  "is_complete": false,
  "targets": [...],
  "created_at": "2024-11-19T20:00:00Z",
  "updated_at": "2024-11-19T20:00:00Z"
}
```

**Invalid: Assign Cat Already on Active Mission:**
```bash
# First assignment (should succeed)
curl -X PATCH http://localhost:8000/api/missions/1/assign_cat/ \
  -H "Content-Type: application/json" \
  -d '{"cat_id": 1}'

# Second assignment to same cat (should fail)
curl -X PATCH http://localhost:8000/api/missions/2/assign_cat/ \
  -H "Content-Type: application/json" \
  -d '{"cat_id": 1}'
```

**Error Response:**
```json
{
  "cat_id": [
    "Cat is already assigned to an active mission."
  ]
}
```

### 3. Update Mission Target - Update Notes

**Endpoint:** `PATCH /api/missions/{mission_id}/targets/{target_id}/`

```bash
curl -X PATCH http://localhost:8000/api/missions/1/targets/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "notes": "Target spotted at coordinates 51.5074, -0.1278. Proceeding with surveillance."
  }'
```

**Response:**
```json
{
  "notes": "Target spotted at coordinates 51.5074, -0.1278. Proceeding with surveillance.",
  "is_complete": false
}
```

### 4. Update Mission Target - Mark as Complete

**Endpoint:** `PATCH /api/missions/{mission_id}/targets/{target_id}/`

```bash
curl -X PATCH http://localhost:8000/api/missions/1/targets/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "is_complete": true
  }'
```

**Response:**
```json
{
  "notes": "Target spotted at coordinates 51.5074, -0.1278. Proceeding with surveillance.",
  "is_complete": true
}
```

### 5. Invalid: Update Notes on Completed Target (Should Fail)

```bash
# First, mark target as complete
curl -X PATCH http://localhost:8000/api/missions/1/targets/1/ \
  -H "Content-Type: application/json" \
  -d '{"is_complete": true}'

# Then try to update notes (should fail)
curl -X PATCH http://localhost:8000/api/missions/1/targets/1/ \
  -H "Content-Type: application/json" \
  -d '{"notes": "Trying to update completed target"}'
```

**Error Response:**
```json
{
  "non_field_errors": [
    "Cannot update notes on a completed target."
  ]
}
```

### 6. Test Auto-Complete Mission

```bash
# Create mission with 2 targets
curl -X POST http://localhost:8000/api/missions/ \
  -H "Content-Type: application/json" \
  -d '{
    "targets": [
      {"name": "Target 1", "country": "USA", "notes": ""},
      {"name": "Target 2", "country": "UK", "notes": ""}
    ]
  }'

# Complete first target
curl -X PATCH http://localhost:8000/api/missions/1/targets/1/ \
  -H "Content-Type: application/json" \
  -d '{"is_complete": true}'

# Complete second target (mission should auto-complete)
curl -X PATCH http://localhost:8000/api/missions/1/targets/2/ \
  -H "Content-Type: application/json" \
  -d '{"is_complete": true}'

# Check mission status
curl -X GET http://localhost:8000/api/missions/1/
```

**Response (mission is_complete should be true):**
```json
{
  "id": 1,
  "cat": null,
  "cat_name": null,
  "is_complete": true,
  "targets": [
    {
      "id": 1,
      "name": "Target 1",
      "country": "USA",
      "notes": "",
      "is_complete": true,
      ...
    },
    {
      "id": 2,
      "name": "Target 2",
      "country": "UK",
      "notes": "",
      "is_complete": true,
      ...
    }
  ],
  ...
}
```

### 7. Invalid: Update Notes on Target of Completed Mission

```bash
# After all targets are complete, mission is auto-completed
# Try to update notes on any target (should fail)
curl -X PATCH http://localhost:8000/api/missions/1/targets/1/ \
  -H "Content-Type: application/json" \
  -d '{"notes": "Trying to update after mission complete"}'
```

**Error Response:**
```json
{
  "non_field_errors": [
    "Cannot update notes on a target of a completed target."
  ]
}
```

### 8. List All Missions

**Endpoint:** `GET /api/missions/`

```bash
curl -X GET http://localhost:8000/api/missions/
```

**Response:**
```json
{
  "count": ...,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "cat": 1,
      "cat_name": "Agent Whiskers",
      "is_complete": false,
      "targets": [...],
      "created_at": "2024-11-19T20:00:00Z",
      "updated_at": "2024-11-19T20:00:00Z"
    },
    ...
  ]
}
```

### 9. Get a Single Mission

**Endpoint:** `GET /api/missions/{id}/`

```bash
curl -X GET http://localhost:8000/api/missions/1/
```

**Response:**
```json
{
  "id": 1,
  "cat": 1,
  "cat_name": "Agent Whiskers",
  "is_complete": false,
  "targets": [
    {
      "id": 1,
      "name": "Target Alpha",
      "country": "USA",
      "notes": "Intelligence gathered",
      "is_complete": false,
      "created_at": "2024-11-19T20:00:00Z",
      "updated_at": "2024-11-19T20:00:00Z"
    }
  ],
  "created_at": "2024-11-19T20:00:00Z",
  "updated_at": "2024-11-19T20:00:00Z"
}
```

### 10. Delete a Mission (Not Assigned to Cat)

**Endpoint:** `DELETE /api/missions/{id}/`

```bash
# Delete mission without assigned cat (should succeed)
curl -X DELETE http://localhost:8000/api/missions/2/
```

**Response:** `204 No Content`

### 11. Invalid: Delete Mission Assigned to Cat (Should Fail)

```bash
# Create mission and assign cat
curl -X POST http://localhost:8000/api/missions/ \
  -H "Content-Type: application/json" \
  -d '{
    "targets": [{"name": "Target", "country": "USA", "notes": ""}]
  }'

curl -X PATCH http://localhost:8000/api/missions/3/assign_cat/ \
  -H "Content-Type: application/json" \
  -d '{"cat_id": 1}'

# Try to delete (should fail)
curl -X DELETE http://localhost:8000/api/missions/3/
```

**Error Response:**
```json
{
  "error": "Cannot delete a mission assigned to a cat."
}
```

---

## Complete Testing Workflow

```bash
# 1. Create spy cats with valid breeds
curl -X POST http://localhost:8000/api/cats/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Agent A", "years_of_experience": 5, "breed": "Siamese", "salary": 50000}'

curl -X POST http://localhost:8000/api/cats/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Agent B", "years_of_experience": 3, "breed": "Persian", "salary": 45000}'

# 2. Test invalid breed
curl -X POST http://localhost:8000/api/cats/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Agent C", "years_of_experience": 4, "breed": "FakeCat", "salary": 40000}'

# 3. List all cats
curl -X GET http://localhost:8000/api/cats/

# 4. Update cat salary
curl -X PATCH http://localhost:8000/api/cats/1/ \
  -H "Content-Type: application/json" \
  -d '{"salary": 55000}'

# 5. Create mission with 2 targets
curl -X POST http://localhost:8000/api/missions/ \
  -H "Content-Type: application/json" \
  -d '{
    "targets": [
      {"name": "Target 1", "country": "USA", "notes": "Initial notes"},
      {"name": "Target 2", "country": "UK", "notes": ""}
    ]
  }'

# 6. Assign cat to mission
curl -X PATCH http://localhost:8000/api/missions/1/assign_cat/ \
  -H "Content-Type: application/json" \
  -d '{"cat_id": 1}'

# 7. Update target notes
curl -X PATCH http://localhost:8000/api/missions/1/targets/1/ \
  -H "Content-Type: application/json" \
  -d '{"notes": "Updated intelligence data"}'

# 8. Complete first target
curl -X PATCH http://localhost:8000/api/missions/1/targets/1/ \
  -H "Content-Type: application/json" \
  -d '{"is_complete": true}'

# 9. Try to update notes on completed target (should fail)
curl -X PATCH http://localhost:8000/api/missions/1/targets/1/ \
  -H "Content-Type: application/json" \
  -d '{"notes": "Should not work"}'

# 10. Complete second target (mission auto-completes)
curl -X PATCH http://localhost:8000/api/missions/1/targets/2/ \
  -H "Content-Type: application/json" \
  -d '{"is_complete": true}'

# 11. Verify mission is complete
curl -X GET http://localhost:8000/api/missions/1/

# 12. Try to delete assigned mission (should fail)
curl -X DELETE http://localhost:8000/api/missions/1/

# 13. Create unassigned mission
curl -X POST http://localhost:8000/api/missions/ \
  -H "Content-Type: application/json" \
  -d '{"targets": [{"name": "Test", "country": "USA", "notes": ""}]}'

# 14. Delete unassigned mission (should succeed)
curl -X DELETE http://localhost:8000/api/missions/2/
```

## Valid Cat Breeds (Sample)

Some valid breeds from TheCatAPI:
- Abyssinian
- American Bobtail
- American Shorthair
- Bengal
- British Shorthair
- Egyptian Mau
- Maine Coon
- Persian
- Ragdoll
- Russian Blue
- Scottish Fold
- Siamese
- Sphynx

Note: The API validates against the complete list from https://api.thecatapi.com/v1/breeds