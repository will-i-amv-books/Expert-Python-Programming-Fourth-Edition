# Modern Python Development Environments

## Python's packaging ecosystem

### Installing Python packages using pip

Installing a new package with pip:

    $ pip install <package-name>

Check pip's available options:

    $ pip --help

### Isolating the runtime environment

Inspect paths where Python will search for modules and packages:

    $ python3 -m site

Installing packages from PyPI into the global site-packages directory 
is not recommended and should be avoided:

* Python is an important part of many packages that are available 
  through operating system package repositories and power a lot of important services.

* Python packages that are available from a system's package repositories
  (apt, yum, or rpm) contain custom patches or are purposely kept outdated to
  ensure compatibility with other system components. 

* Forcing an update of such packages, using pip, to a version that breaks 
  backward compatibility might cause bugs in crucial system services.

There is an solution to this problem: environment isolation. 
The benefits of this approach are as follows:

* It solves the project X depends on package 1.x but project Y needs package 4.x dilemma. 

* The project is no longer constrained by versions of packages that are
  provided in the developer's system distribution repositories.

* There is no risk of breaking other system services that depend on certain package versions, 
  because new package versions are only available inside such an environment.

* A list of packages that are project dependencies can be easily locked.

### Application-level environment isolation

Create a new virtual environment:

    $ python3.X -m venv <env-name>

Activate the virtual environment:
    
    $ source <env-name>/bin/activate

Best practices with virtual envs:

* They are not portable and should not be moved to another system/machine or even a different filesystem path.

* Thy are useful for writing focused libraries that are independent of the operating system 
  or projects of low complexity that don't have too many external dependencies.

A best practice used by pip users is to store the definition of all project dependencies in a single file 'requirements.txt'.
You can install the dependencies using the -r flag to specify the file path:
    
    $ pip install -r requirements.txt

Best practices with requitements.txt file:

* Pinned version specifiers are best for reproducibility

* For projects that are well tested with different dependency versions, 
  version ranges are acceptable

* Packages without versions should be avoided unless latest release is always required

### Poetry as a dependency management system

Poetry can be installed using pip:
    
    $ pip install --user poetry

Create a completely new project:

    $ poetry new <my-project-name>

Initialize an existing project:

    $ cd <my-project-name>
    $ poetry init

If you create a new project or initialize an existing one using Poetry, 
it will create a new virtual environment in a shared location.
You can activate it as follows:

    $ cd <my-project-name>
    $ poetry shell

Install a new dependency to your project:
    
    $ poetry add <package-name>

When your environment has a working and tested set of package versions, 
create a lock file:
    
    $ poetry lock

### System-level environment isolation

Advantages:

* The development environment can exactly match the system version, services, 
  and shared libraries used in production, which helps to solve compatibility issues.

* Definitions for system configuration tools (if used) can be reused 
  to configure both the production and development environments.

* The newly hired team members can easily hop into the project 
  if the creation of such environments is automated.

### Virtual environments using Docker

Dockerfiles:

* A Dockerfile is a description of how to create a Docker image.    

* A Docker image is described in the Dockerfile by instructions in the format:
    INSTRUCTION arguments

Docker basic instructions:

* FROM <image-name>: This describes the base image that your image will be based on. 

* COPY <src> <dst>: This copies files from the local filesystem to the container's filesystem.
* ADD <src> <dst>: Similar to COPY but automatically unpacks archives and allows URLs in <src>.
* RUN <command>: Runs a specified command on top of previous layers.
* ENTRYPOINT ["<executable>", "<param>", ...]: 
  Configures the default command to be run as your container starts (/bin/sh -c by default)
* CMD ["<param>", ...]: 
  Specifies the default parameters for image entry points. 
* WORKDIR <dir>: Sets the current working directory for the next instructions.

Build Docker image:

    $ docker build -t <name> <path>

List all Docker images:

    $ docker images

Create a network:
    
    $ docker network create <my-network-name>

An example of running a Docker image in interactive mode: 
    
    $ docker run -it --rm --publish 5000:5000 echo

Explanation of the above argument options:

* The -i (for interactive) keeps STDIN open, even if the container process is detached. 

* The -t (for tty) allocates pseudo-TTY for the container. 

* The --rm Tells Docker to automatically remove the container when it exits.

* The --publish 5000:5000  tells Docker to publish the container's port 5000 
  by binding port 5000 on the host's interface. 

Docker Compose

* It allows you to describe multi-container applications using the YAML syntax.

* There are 2 main commands:
    - docker compose up: Starts all containers defined in the docker-compose.yml file and actively prints their standard output.
    - docker compose down: Stops all containers started by docker-compose in the current project directory.
