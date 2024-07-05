class ADLSPathBuilder:
    @staticmethod
    def get_container_url(storage_account_name, container_name):
        """
        Generate the URL for a given container in the storage account.
        
        :param storage_account_name: Name of the storage account.
        :param container_name: Name of the container.
        :return: Container URL as a string.
        """
        return f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/"

    @staticmethod
    def get_folder_path(storage_account_name, container_name, folder_name):
        """
        Generate the full path for a specific folder within a container.
        
        :param storage_account_name: Name of the storage account.
        :param container_name: Name of the container.
        :param folder_name: Name of the folder.
        :return: Full path to the folder as a string.
        """
        container_url = ADLSPathBuilder.get_container_url(storage_account_name, container_name)
        return f"{container_url}{folder_name}/"
