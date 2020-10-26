#  Copyright 2020 Markus Liljergren
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import glob
import shutil
import pygit2
import logging
import os
from os.path import basename
import shutil

log = logging.getLogger(__name__)


def is_clean(repo):
    status = repo.status()
    for filepath, flags in status.items():
        if flags != pygit2.GIT_STATUS_CURRENT:
            if flags != 16384:
                return False
    return True


def copy_files_by_wildcard(source_path, target_path):
    for file in glob.glob(source_path):
        log.info(file + ':' + target_path)
        if (not os.path.exists(target_path)):
            (head, tail) = os.path.split(target_path)
            if(not '.' in tail):
                log.warn('Creating folder: ' + target_path)
                os.makedirs(target_path)
            elif(not os.path.exists(head)):
                log.warn('Creating head folder: ' + head)
                os.makedirs(head)
        shutil.copy(file, target_path)

def zipFolder(root_path, base_dir, target_file):
    shutil.make_archive(target_file, 'zip', root_path, base_dir)
    # with ZipFile(target_file, 'w') as zipObj:
    #   # Iterate over all the files in directory
    #   for folderName, subfolders, filenames in os.walk(source_path):
    #       for filename in filenames:
    #           #create complete filepath of file in directory
    #           filePath = os.path.join(folderName, filename)
    #           # Add file to zip
    #           zipObj.write(filePath, basename(filePath))
