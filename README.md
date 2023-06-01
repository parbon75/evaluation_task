
# Evaluation_Task
The answers of the Evaluation tasks for the Blender, Python, JavaScript 3D and Docker

# Technical Exam: Blender, Python, JavaScript 3D, and Docker

## Blender & Python

**Q1.1**: Blender provides an API that can be interacted with using Python. How can you use Python scripting to automate the creation of a 3D model in Blender? Please provide a basic code example.

**Ans**. Blender 3D is a powerful tool that can be used for a wide range of tasks, from 3D modeling and animation to video editing and compositing. With the help of Python scripting and the bpy module, you can automate many of these tasks and create custom workflows that are tailored to your specific needs.

Now that we know how to create and run a basic script, let's take a look at some specific tasks we can automate using bpy.

Creating Objects

One of the most common tasks in Blender 3D is creating and manipulating objects. Here's an example script that creates a new cube and sets its location and scale:

```python
import bpy 
 
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0)) 
cube = bpy.context.active_object 
cube.location = (2, 0, 0) 
cube.scale = (1, 2, 1) 

```
In this script, we use the bpy.ops.mesh.primitive_cube_add() operator to create a new cube object. We then set the location and scale of the cube using the object's location and scale properties.


**Q1.2**: In Blender's Python API, what is the purpose of the bpy module? How can you use it to manipulate object transformations in a 3D scene?

**Ans**. In Blender's Python API, the bpy module is the main module that provides access to Blender's functionality and allows you to manipulate objects, scenes, materials, and other aspects of the 3D scene.

The bpy module acts as a bridge between Blender's user interface and the Python script, allowing you to automate tasks and create custom tools. It provides a wide range of classes, functions, and properties to interact with Blender's data and control its behavior.

To manipulate object transformations in a 3D scene using the bpy module, you can follow these steps:

```python
# Import the 'bpy' module
import bpy

# Access the active object
obj = bpy.context.object

# Select specific objects by name
obj = bpy.data.objects['Cube']

# Change the location
obj.location = (x, y, z)

# Change the rotation (in radians)
obj.rotation_euler = (rx, ry, rz)

# Change the scale
obj.scale = (sx, sy, sz)

# Update the 3D view to reflect the changes
bpy.context.view_layer.update()

```

Additionally, you can perform more advanced transformations, such as parenting objects, applying transformations, or manipulating individual components (e.g., vertices, edges, and faces) using the available methods and properties provided by the bpy module.

Remember to have a valid Blender context, such as an open Blender instance or an active script, to use the bpy module effectively.


## Python & Docker

**Q2.1**: Describe the steps to create a Docker container for a Python-based application. What information would you need to include in the Dockerfile? 

**Ans**. To create a Docker container for a Python-based application, you can follow these steps:

1. Create a Dockerfile: Create a file named "Dockerfile" (without any file extension) in the root directory of your project.

2. Choose a base image: Select a suitable base image that provides the necessary dependencies for running Python applications. 

For example, you can use the official Python Docker image, which provides a variety of Python versions and variants. Specify the desired Python version and variant in the Dockerfile. For example, to use Python 3.9, you can use the following line in the Dockerfile:

```
FROM python:3.9

```

3. Copy application files: Use the COPY instruction in the Dockerfile to copy your application files into the container. Specify the source files or directories from your host machine and the destination directory inside the container. For example, if your application consists of a single file named "app.py," you can copy it into the container using:

```
COPY app.py /app/

```

4. Install dependencies: If your application has dependencies listed in a requirements.txt file, you can use the RUN instruction to install them inside the container. Add the following line in the Dockerfile:

```
RUN pip install -r requirements.txt
```

5. Set the working directory: Use the WORKDIR instruction to set the working directory inside the container. This is where your application will run from. For example:

```
WORKDIR /app
```

6. Expose necessary ports: If your application listens on a specific port, you need to expose that port using the EXPOSE instruction in the Dockerfile. For example, if your application listens on port 8000, add the following line:

```
EXPOSE 8000
```

7. Define the startup command: Use the CMD instruction to specify the command that will be executed when the container starts. For a Python application, the command typically involves running the Python script. For example:

```
CMD ["python", "app.py"]
```

8. Build the Docker image: Open a terminal, navigate to the directory containing the Dockerfile, and run the following command to build the Docker image:
  
```
docker build -t myapp .
```
This command will build the Docker image using the instructions in the Dockerfile. The -t flag is used to specify a tag or name for the image. In this example, the image is named "myapp".

9. Run the Docker container: After the image is built, you can run the Docker container using the following command:

```
docker run myapp
```
The container will be created and your Python application will start running inside it.

When creating the Dockerfile, you need to include the necessary instructions for your specific application, such as copying the required files, installing dependencies, and specifying the startup command. The example steps above provide a general outline, but the specifics may vary depending on the requirements of your Python application.


**Q2.2**: Explain how you can use Docker Compose to manage multi-container Python applications.

**Ans**. Docker Compose is a tool that allows you to define and manage multi-container Docker applications. It simplifies the process of orchestrating multiple containers, their dependencies, and their configurations.

To manage a multi-container Python application using Docker Compose, you can follow these steps:

1. Install Docker Compose: Ensure that Docker Compose is installed on your system. You can download and install it from the official Docker website or use package managers like pip (Python package manager) to install it globally.

2. Define the Docker Compose file: Create a file named "docker-compose.yml" (or any other name you prefer) in the root directory of your project. This file will contain the configuration for your multi-container application.

3. Specify services: In the Docker Compose file, define each service/container that your application requires. Each service will have a unique name and its own configuration. For example, if your application requires a Python web server and a PostgreSQL database, you can define two services like this:

```
version: '3'
services:
  web:
    build: .
    ports:
      - 8000:8000
    volumes:
      - .:/app
  db:
    image: postgres
    environment:
      - POSTGRES_USER=myuser
      - POSTGRES_PASSWORD=mypassword
```
In this example, the "web" service is built using the current directory (.) as the build context, and it exposes port 8000 on the host machine. The "db" service uses the official PostgreSQL image and sets environment variables for the username and password.      

4. Define network and dependencies: If your services need to communicate with each other, you can define a network within Docker Compose and specify the dependencies between services. Docker Compose automatically creates a network for your application, allowing containers to communicate with each other using their service names. For example, if the web service needs to access the database service, you can specify the dependency like this:

```
version: '3'
services:
  web:
    ...
    depends_on:
      - db
  db:
    ...
```

5. Customize service configurations: Docker Compose allows you to customize various aspects of the services, such as environment variables, volumes, and container names. You can add additional configuration options to each service as per your requirements.

6. Run the application: Open a terminal, navigate to the directory containing the Docker Compose file, and run the following command:

```
docker-compose up
```

This command will start the containers defined in the Docker Compose file, create the necessary network, and connect the services. The output of each container will be displayed in the terminal.

Docker Compose provides additional commands and options to manage your multi-container application, such as scaling services, stopping containers, rebuilding images, and more. You can refer to the Docker Compose documentation for more information on these commands and their usage.

By using Docker Compose, you can easily manage the deployment, configuration, and scaling of multi-container Python applications, making it convenient to work with complex application setups and their dependencies.
