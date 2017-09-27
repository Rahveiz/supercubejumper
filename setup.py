import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Super Cube Jumper",
    options={"build_exe": {"packages":["pygame", "maps"],
                           "include_files":["bill.png", "Evolving.mp3", "Forgiven.mp3", "Nova.mp3", "We Don't Know.mp3", "Credits.png", "endgame.png", "carre1.png","Stage 1_1.png","Stage 1_2.png","Stage 1_3.png","Stage 1_4.png","Stage 1_5.png",
    "Stage 2_1.png","Stage 2_2.png","Stage 2_3.png","Stage 2_4.png","Stage 2_5.png",
    "Stage 3_1.png","Stage 3_2.png","Stage 3_3.png","Stage 3_4.png","Stage 3_5.png", "maps.py", "hachicro.ttf" ]}},
    executables = executables

    )