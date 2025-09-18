from visual.window import Window
from visual.sections import ProblemSection, MethodSection

import logic as lg

if __name__ == "__main__":
    f_x = lg.Function("0")

    root = Window()
    root.set_theme()
    root.minsize(800, 600)
    root.goto_center()

    problem_section = ProblemSection(root, f_x)
    problem_section.pack(side="left", padx=10, pady=10, fill="y", expand=False)

    method_section = MethodSection(root)
    method_section.pack(side="left", padx=10, pady=10, fill="both", expand=True)

    root.mainloop()

