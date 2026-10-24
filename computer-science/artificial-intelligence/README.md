# AI and Machine Learning

Python programs from the Artificial Intelligence course, grouped by topic.

## Setup

    pip install -r requirements.txt

Tested with Python 3.12, scikit-learn 1.8, and pgmpy 1.1.2. The Bayesian network programs use `DiscreteBayesianNetwork`, which exists in recent pgmpy versions only.

## Data

Three programs read CSV files that are not stored in this repo:

| File | Used by |
|---|---|
| `customers.csv` | `unsupervised-learning/customer_segmentation_kmeans.py` |
| `students.csv` | `unsupervised-learning/student_clusters_elbow_method.py` |
| `train.csv` | `supervised-learning/house_price_regression.py`, the Kaggle House Prices training file |

Download the Kaggle file from the competition page and place it next to the script.

## Programs

| Topic | Program | What it does |
|---|---|---|
| intelligent-agents | `simple_reflex_agent.py` | Turns a light on or off from brightness and motion input |
| intelligent-agents | `model_based_agent.py` | Cleaning agent that keeps an internal model of three rooms |
| intelligent-agents | `goal_based_delivery_robot.py` | Robot that moves through a warehouse toward a delivery goal |
| intelligent-agents | `utility_based_assistant.py` | Compares a fast expensive option with a slow cheap one by utility |
| uninformed-search | `depth_limited_search_agent.py` | Agent that finds a goal with depth limited search |
| uninformed-search | `uniform_cost_search_agent.py` | Agent that finds the cheapest path with uniform cost search |
| uninformed-search | `uniform_cost_search.py` | Uniform cost search as a plain function with path and total cost |
| uninformed-search | `iterative_deepening_dfs.py` | Iterative deepening search on a tree and on a graph |
| constraint-satisfaction | `course_timetable.py` | Assigns four courses to slots with all different and restriction rules |
| constraint-satisfaction | `sudoku_4x4.py` | Solves a 4 by 4 Sudoku with OR-Tools |
| constraint-satisfaction | `exam_slot_scheduling.py` | Schedules exams in slots while minimizing late exams |
| local-search | `beam_search.py` | Beam search on a weighted graph, level by level |
| local-search | `hill_climbing_8_queens.py` | Hill climbing with random restarts for 8 queens |
| local-search | `genetic_algorithm_timetable.py` | Genetic algorithm for a teacher and course timetable |
| adversarial-search | `minimax.py` | Minimax on a small game tree |
| adversarial-search | `alpha_beta_pruning.py` | Alpha beta pruning on the same kind of tree |
| adversarial-search | `minimax_with_heuristic.py` | Minimax with a heuristic for an agent racing to a goal |
| adversarial-search | `tic_tac_toe_alpha_beta.py` | Tic tac toe against an alpha beta player |
| bayesian-networks | `hiring_decision.py` | Hiring decision from education, experience, and interview |
| bayesian-networks | `car_fault_diagnosis.py` | Diagnoses a car fault from symptoms |
| bayesian-networks | `online_purchase.py` | Purchase probability from ads, website experience, and price |
| supervised-learning | `student_score_regression.py` | Linear regression for a final score |
| supervised-learning | `loan_approval_decision_tree.py` | Decision tree with feature selection for loan approval |
| supervised-learning | `customer_churn_random_forest.py` | Random forest for customer churn |
| supervised-learning | `house_price_regression.py` | Linear regression on house prices with exploration and plots |
| unsupervised-learning | `customer_segmentation_kmeans.py` | K means on customers, with and without scaling |
| unsupervised-learning | `vehicle_clustering_kmeans.py` | K means on vehicle data with encoded types |
| unsupervised-learning | `student_clusters_elbow_method.py` | Chooses k with the elbow method on student data |
