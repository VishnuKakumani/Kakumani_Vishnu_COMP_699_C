# Ultimate Python Code Insight Lab

## Overview
**Ultimate Python Code Insight Lab** is a comprehensive Python-based platform designed to provide deep insights into Python code. It integrates coding style analysis, algorithm benchmarking, safe mutation simulations, and emotional visualization of code characteristics into a unified system. The platform helps developers, teams, and educators improve code quality, optimize performance, and understand coding behavior through detailed analytics and interactive dashboards.

This project is implemented entirely using **Python**, **Streamlit**, and Python libraries, ensuring local computation without external dependencies. Users can upload Python scripts or multiple algorithm variants for detailed analysis, compare algorithm performance, simulate safe mutations, and visualize code characteristics over time.


## Features

- **Code Analysis**
  - Extracts code structure, including functions, classes, and control flows.
  - Analyzes naming consistency, commenting, and coding patterns.
  - Generates developer personality profiles based on coding style.

- **Algorithm Benchmarking**
  - Measures runtime performance, memory usage, recursion depth, branching complexity, and error-proneness.
  - Provides a ranked comparison of multiple algorithm variants.
  - Suggests the best-performing algorithm variant.

- **Safe Mutation and Evolution**
  - Simulates code mutations such as variable renaming, loop restructuring, and function inlining without changing logic.
  - Predicts impact on runtime, readability, and efficiency.
  - Tracks algorithm evolution over multiple simulated generations.
  - Annotate or tag preferred algorithm versions for reuse.

- **Code Emotional Mapping**
  - Visualizes mood-like characteristics of code (e.g., elegant, chaotic, stressed, playful).
  - Generates dashboards combining personality, performance, mutation, and emotional insights.
  - Tracks trends across multiple submissions for historical improvement visualization.

- **User Roles**
  - **Developer**: Upload scripts, benchmark algorithms, analyze coding style, and perform safe mutations.
  - **Team Lead**: Compare coding styles, team performance, and track improvement trends.
  - **Educator**: Evaluate student submissions, generate grading reports, and visualize class-wide performance.
  - **Administrator**: Manage users, roles, and system-level permissions.

---

## Technologies Used

- **Language**: Python 3.x  
- **Framework**: Streamlit (for interactive dashboards and visualization)  
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, NetworkX (for visualization), and other standard Python libraries for analysis and computation.  

The system runs entirely locally and does not require external services or cloud dependencies, ensuring privacy and security for uploaded code.

---

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/ultimate-python-code-insight-lab.git
2. Navigate to the project folder:
   cd ultimate-python-code-insight-lab
3. Install dependencies:
   pip install -r requirements.txt
4. Run the Streamlit app:
   streamlit run app.py



