# General switches and paths
DATA_DIR = "c:/Users/Admin/Desktop/DataScience/Main/Student_success/data"

ENROLLMENT_CSV = f"{DATA_DIR}/enrollment.csv"    # must contain target column: 'enrolled'
ACADEMICS_CSV  = f"{DATA_DIR}/academics.csv"     # GPA, course completions, fails, etc.
DEMOS_CSV      = f"{DATA_DIR}/demographics.csv"  # age, gender, location, SES, etc.

# Primary keys to merge datasets
PRIMARY_KEY = " student_id "

# Targets
TARGET_ENROLL = "enrolled"  # binary {0,1}
TARGET_SUPPORT = "needs_support"  # binary {0,1} (set SUPPORT_AS_REGRESSION=True for regression)

SUPPORT_AS_REGRESSION = False  # set True if you have continuous label like "support_intensity"

# Feature blocks (update to your schema)
CATEGORICAL_COLS = [
    "gender", "location_region", "ses_bracket", "program_applied",
]
NUMERIC_COLS = [
    "age", "hs_gpa", "standardized_score", "application_lead_days",
    "current_gpa", "credits_completed", "courses_failed",
    "attendance_rate", "support_sessions_attended",
    "scholarship_amount", "tuition_balance"
]
# Optional date fields for time features
DATE_COLS = ["application_date", "enrollment_date"]

# Model params
RANDOM_STATE = 42
TEST_SIZE = 0.2
N_JOBS = -1