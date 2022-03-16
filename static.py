


sender = 'pikrust2022+python@gmail.com'

receiver = 'mthartz25@gmail.com'


subject = 'Test Subject'

email_lock = 'pythontest'

exercises_per_workout = {'biceps': 4, 'triceps': 4, 'legs': 4, 'shoulders' : 4,
                         'chest': 4, 'abs': 4, 'back': 4, 'corrective' : 2}

bicep_exercises = ['barbell_curl', 'dumbbell_curl', '7s', 'cable_curl', 'high_cable_curl', 'reverse_curl']

tricep_exercises = ['cable_pushdown', 'cable_pushaway', 'tricep_press_machine', 'cobra_pushup','reverse_grip_pushdown',
                'JM_press', 'dumbell_kickback', 'bench_tricep_extension', 'tricep_dip', 'closegrip_bench_press']


legs_exercises = ['back_squat', 'barbell_reverse_lunges', 'cable_pullthroughs', 'dumbbell_reverse_lunges', 'dumbbell_sprinter_lunges',
                'calf_raises', 'leg_extension', 'banded_frog_press', 'bulgarian_squats', 'bulgarian_plyos', '1_leg_bench_squats']


chest_exercises = ['barbell_bench_press', 'dumbbell_bench_press', 'cable_crossover', 'pushups', 'decline_pushups', 'plate_squeeze',
                    'bench_pullovers', 'incline_barbell_press', 'incline_dumbbell_press', 'chest_dip', 'ucv_raise']

back_exercises = ['cable_lat_pulldown', 'bench_lat_raise', 'machine_lat_pulldown', 'machine_rows', 'cable_bar_pulldowns']

corrective_exercises = ['face_pulls', 'clam_shells', 'rhomboid_pulls']

shoulders_exercises = ['barbell_OHP', 'dumbbell_OHP', 'lateral_raises', 'reverse_flys', 'front_raises', 'arnold_press', 'rear_delt_row',
                    'cable_lateral_raise', 'scoop_press']


#do i want to store workouts in a dictionary or a list? If in a dictionary i could do list comprehension each
#time I do a random sample of the values. Do I want to incorporate random weights into the random sample?