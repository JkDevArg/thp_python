import os

def add_log(log_list, message):
    log_list.append(message)

def export_log(log_list, filename):
    if not filename.endswith(''):
        filename += ''

    log_dir = "log"
    os.makedirs(log_dir, exist_ok=True)
    file_path = os.path.join(log_dir, filename)

    with open(file_path, 'w') as f:
        f.write('\n'.join(log_list))
