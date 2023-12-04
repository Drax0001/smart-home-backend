# Instructions on how to install it

###  First Clone the repo: `git clone 'repo link'`

###  install the dependencies: `pip install flask pymongo`

###  The server runs on: `http://127.0.0.1:5000`

#### Use ChatGPT to help you figure out how to consume the endpoints present in the backend

# Content of the code

#### In this codebase, there are two endpoints, the backend is connected to mongodb database.

The two endpoints are:
- `/get_lights`: a `GET` request that fetches the states of all the lights in the database. returns data in the format: 
  ```
  [
    {
        "location": "kitchen",
        "state": true
    },
    {
        "location": "bathroom",
        "state": false
    },
    {
        "location": "bedroom",
        "state": false
    },
    {
        "location": "living_room",
        "state": false
    },
    {
        "location": "veranda",
        "state": false
    }
  ] 
  ```
- `/toggle_light`: a `POST` request endpoint to toggle the a particular light, on or off. Here, the frontend sends a `JSON` object to the backend in the following format:
    ```
        {
            "location": "kitchen",
            "state": true
        }
    ```
When this request is made, the backend responds back with `JSON` in the following format:
  ```
    {
        "location": "veranda",
        "state": true,
        "success": true
    }
  ```

**The above info should be fed back to the frontend to update the UI**