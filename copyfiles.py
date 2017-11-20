import os, shutil
import send2trash

class CopyFiles():
    """docstring for CopyFiles"""

    def __init__(self, arg):
        super(CopyFiles, self).__init__()
        self.arg = arg

    def copy_single_file(self, file):
        """
        :param file:
        :return:
        """
        pass

    def copy_tree_of_files(self, files):
        """

        :param files:
        :return:
        """
        pass

    def move_single_file(self, file, location):
        """
		Move a single file to another location
		:param file: file, Location: location to which file need to go
		:return:
		"""
        pass

    def perm_delete_single_file(self, file):
        """
		Perm delete a single file
		:param file:
		:return:
		"""
        pass

    def perm_delete_tree_of_files(self, files):
        """
		Perm delete a tree of files
		:param files:
		:return:
		"""
        pass

    def soft_delete_single_file(self, file):
        """
		Soft delete a file, this sends the file to the trash can.
		:param file:
		:return:
		"""
        pass

	def restore_single_file(self, file):
		"""
		Restore a single file
		:param self:
		:param file:
		:return:
		"""
		pass
    
    def rename_every_file_in_tree(self, location):
        """
        Rename every file in folder or subfolder tree
        :param location:
        :return:
        """
        pass
    