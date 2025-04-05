import subprocess
import uuid
import os


def is_docker_running() -> bool:
    try:
        subprocess.run(["sudo", "docker", "info"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        print("Docker is not installed.")
        return False


def build_docker_image(runtime: str) -> None:
    if runtime == "python":
        image = "lambda-python"
        dockerfile_path = "lambda-serverless-backend/functions/python"
    elif runtime == "javascript":
        image = "lambda-js"
        dockerfile_path = "lambda-serverless-backend/functions/javascript"
    else:
        raise ValueError("Unsupported runtime")

    print(f"Building Docker image for {runtime}...")
    try:
        subprocess.run([
            "sudo", "docker", "build", "-t", image, dockerfile_path
        ], check=True)
        print(f"Image {image} built successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to build Docker image {image}. Error:\n{e}")


def run_function_docker(runtime: str, function_file_path: str, timeout: int = 5) -> bool:
    container_name = f"lambda-{uuid.uuid4()}"

    if runtime == "python":
        image = "lambda-python"
        entry_command = ["arg1", "arg2"]
    elif runtime == "javascript":
        image = "lambda-js"
        entry_command = ["arg1", "arg2"]
    else:
        raise ValueError("Unsupported runtime. Must be 'python' or 'javascript'.")

    abs_file_path = os.path.abspath(function_file_path)
    abs_dir = os.path.dirname(abs_file_path)

    print(f"\nRunning {runtime} function from: {abs_file_path}")
    try:
        result = subprocess.run([
            "sudo", "docker", "run", "--rm", "--name", container_name,
            "-v", f"{abs_dir}:/app",
            image
        ] + entry_command,
        timeout=timeout, capture_output=True, text=True)

        if result.returncode == 0:
            print("Function executed successfully!")
            print("STDOUT:\n" + result.stdout)
            return True
        else:
            print("Function execution failed!")
            print("STDOUT:\n" + result.stdout)
            print("STDERR:\n" + result.stderr)
            return False

    except subprocess.TimeoutExpired:
        print("Execution timed out!")
        return False
    except Exception as e:
        print(f"Error running function: {e}")
        return False


def remove_docker_images(images):
    for image in images:
        print(f"\nRemoving Docker image: {image}")
        try:
            subprocess.run(["sudo", "docker", "rmi", "-f", image], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(f"Image {image} removed.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to remove image {image}. Error: {e.stderr}")


if __name__ == "__main__":
    print("Checking Docker status...")
    if not is_docker_running():
        print("Docker daemon is not running. Please start Docker and try again.")
        exit(1)

    print("\n======================")
    print("Testing Python Function")
    print("======================")
    build_docker_image("python")
    run_function_docker("python", "lambda-serverless-backend/functions/python/function.py")

    print("\n==========================")
    print("Testing JavaScript Function")
    print("==========================")
    build_docker_image("javascript")
    run_function_docker("javascript", "lambda-serverless-backend/functions/javascript/function.js")

    print("\n==========================")
    print("Cleaning up Docker images")
    print("==========================")
    remove_docker_images(["lambda-python", "lambda-js"])
