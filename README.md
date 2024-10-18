# Flask MongoDB Application

This is a simple Flask application that connects to a MongoDB database and allows users to submit their information through a form. The submitted data is then stored in the MongoDB database. **The application is deployed on Kubernetes using Epinio.**

## Features

- Users can submit their name, email, and password through a form.
- The data is stored in a MongoDB database.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your local machine.
- Epinio CLI installed and configured to deploy applications.
- A Kubernetes cluster set up and accessible.
- MongoDB service configured in Epinio.

## Installation

1. **Clone the repository:**

   ```sh
   git clone 
   cd 
   ```

2. **Create a namespace:**
```sh
epinio namespace create test-namespace
```

3. **set the target namespace:**
```sh
epinio namespace target test-namespace
```

4. **push the app:**
   Use the following command to push:
   ```sh
   epinio app push mongo-app .       # . mentions to inculde the current directory
   ```

5. **Set up the environment variable for the app:**

   Use the following command to set the environment variable for your app:

   ```sh
   epinio app env set mongo-app MONGODB_URI "mongodb://root:uE80oiXQbc@x923f79c46ef0b2ffe27133a9bbe2-mongodb.new-namespace.svc.cluster.local:27017/"
   ```

6. **To view the existing Service catlog:**

```sh
 epinio service catalog
```

7. **To create Service:**

```sh
epinio service create mongodb-dev test-svc
```


8. **Bind the MongoDB service to your application:**

   Make sure your application can access the MongoDB service by running:

   ```sh
   epinio app bind mongo-app test-svc
   ```

9. **Check the deployment status:**

   Use the following command to verify that the application is running:

   ```sh
   epinio app show mongo-app
   ```

10. ## Accessing the Application

Once the application is deployed, view the app details:

```sh
epinio app show mongo-app
```

## Project Structure

```plaintext
.
├── static
│   └── styles.css          # Your static files (CSS, JS, images)
├── templates
│   ├── index.html          # The form for user input
│   └── response.html       # The response page after form submission
├── mongo.py                # The main application file
├── test.py                 # The MongoDB connection test file
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Usage

1. Navigate to the Epinio route for your application.
2. Fill out the form with your name, email, and password.
3. Click the submit button.
4. If all fields are filled out correctly, you will be redirected to the response page.

## Contributing

To contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the original branch: `git push origin feature/your-feature-name`.
5. Create a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you want to contact me, you can reach me at [achanandhi.m@gmail.com](mailto:achanandhi.m@gmail.com).

---

### Instructions

1. **Replace placeholders** such as `yourusername`, `your-repo-name`, and `your-email@example.com` with your actual information.
2. **Create a `requirements.txt` file** by running `pip freeze > requirements.txt` in your virtual environment.
3. **Push to GitHub**:

   ```sh
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

