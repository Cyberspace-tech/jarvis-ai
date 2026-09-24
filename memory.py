def save_chat(user, reply):

    with open(
        "data/logs.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"USER: {user}\n"
        )

        file.write(
            f"JARVIS: {reply}\n\n"
        )