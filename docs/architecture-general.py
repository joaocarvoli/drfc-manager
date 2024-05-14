from diagrams import Cluster, Diagram, Edge
from diagrams.aws.robotics import Robomaker
from diagrams.aws.ml import Sagemaker
from diagrams.custom import Custom
from diagrams.onprem.client import User
from diagrams.programming.language import Python
from diagrams.onprem.container import Docker

graph_attr = {
    "fontsize": "20",
    "bgcolor": "transparent"
}

with Diagram("Architecture Diagram", outformat="svg", graph_attr=graph_attr):
    user = User()
    with Cluster("On Premise Server"):
        with Cluster("Jupyter Environment"):
            jupyter_notebook = Custom("Jupyter Notebook", "./assets/jupyter-logo.png")
            libs = Python("Built modules")
        
        docker = Docker()
            
        with Cluster("Containers"):
            minio = Custom("Minio", "./assets/minio-logo.png")
            sagemaker = Sagemaker("drfc-image")
            robomaker = Robomaker("drfc-image")
            
            sagemaker - Edge(color="firebrick", style="dashed") - robomaker
            sagemaker - Edge(color="firebrick", style="dashed") - minio
    
    user >> jupyter_notebook >> libs >> docker >> [sagemaker, robomaker, minio]
