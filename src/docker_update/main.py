import os
import json
import pprint
import argparse

ENV_DATA_FILE_NAME = 'env_data'
CONTAINERS_DIR = '/host/var/lib/docker/containers'
DOCKER_JSON_FILE = 'config.v2.json'

pp = pprint.PrettyPrinter(width=41, compact=True)

## !!! Update following dictionary
env_data = {

}

def read_env():
    if not env_data:
        env_file_path = os.path.join(os.path.dirname(__file__), f'./{ENV_DATA_FILE_NAME}')
        if os.path.exists(env_file_path) :
            with open(env_file_path) as file:
                vars_dict = dict(
                    tuple(line.replace('\n', '').split('=')) for line in file.readlines() if not line.startswith('#')
                )
            return vars_dict
        else:
            return {}
    else:
        return env_data

'''
TODO: some try/except error handling will be useful, for now leave it for younger generation
'''  

def main(container_list):
    envs = read_env()
    print('[+] envs for update ', envs)
    if envs:
        #read all folders with containers
        containers_dirs = [name for name in os.listdir(CONTAINERS_DIR) if os.path.isdir(os.path.join(CONTAINERS_DIR, name))]
        if container_list:
            containers_dirs_filtered = filter(lambda container: container.startswith(tuple(container_list)), containers_dirs)
            containers_dirs_filtered = list(containers_dirs_filtered)
        else:
            containers_dirs_filtered = containers_dirs
        print('[+] containers to be updated ', containers_dirs_filtered)
        for dir in containers_dirs_filtered:
            with open(os.path.join(os.path.dirname(__file__), f'{CONTAINERS_DIR}/{dir}/{DOCKER_JSON_FILE}'), 'r+') as file:
                ## walk env variables and check docker json file
                json_config = json.load(file)
                for key, val in envs.items():
                    env_var = f'{key}={val}'
                    env_list = json_config['Config']['Env']
                    indices = [i for i, x in enumerate(env_list) if x.startswith(key)]
                    if len(indices) == 0:
                        env_list.append(env_var)
                    else:    
                        for ind in indices:
                            env_list[ind] = env_var
                    json_config['Config']['Env'] = env_list
                # update the file with the new envs
                updated_file = json.dumps(json_config)
                file.seek(0)
                file.write(updated_file)
                file.truncate()
        print('Environment variables updated, GOOD JOB !')
    else:
        print('No environment variable has been provided for update !')

if __name__ == '__main__':
    # main()
    args_parser = argparse.ArgumentParser(description='Container list which will be updated')
    args_parser.add_argument('-l', type=str, nargs='*')
    containers = args_parser.parse_args()
    container_list = []
    if containers.l:
        container_list = containers.l
    main(container_list)