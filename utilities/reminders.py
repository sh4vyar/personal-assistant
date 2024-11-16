reminders_list = []

def add_reminder(reminder):
    reminders_list.append(reminder)
    return "Reminder added."

def list_reminders():
    if not reminders_list:
        return "You have no reminders."
    return "\n".join([f"{i+1}. {rem}" for i, rem in enumerate(reminders_list)])
