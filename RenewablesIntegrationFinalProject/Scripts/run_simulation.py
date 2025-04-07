from pydss import dss as pyDSS
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
SCENARIO = "default"

def run_simulation():
    pydss = pyDSS(
        project_path=os.path.join(PROJECT_DIR, "project.json"),
        scenario=SCENARIO
    )
    pydss.run_simulation()
    print("Simulation completed!")

if __name__ == "__main__":
    run_simulation()