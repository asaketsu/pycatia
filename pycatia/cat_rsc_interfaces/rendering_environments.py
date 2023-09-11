#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_rsc_interfaces.rendering_environment import RenderingEnvironment
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class RenderingEnvironments(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     RenderingEnvironments
                | 
                | A collection of all the Rendering Environments objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=RenderingEnvironment)
        self.rendering_environments = com_object

    def add(self, i_environment_type: int) -> RenderingEnvironment:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add(short iEnvironmentType) As RenderingEnvironment
                | 
                |     Adds a new environment to the environments collection.
                | 
                |     Parameters:
                | 
                |         iEnvironmentType
                |             The type of the environment to create choosen
                |             among:
                | 
                |             1 - For cubical environment
                |             2 - For spherical environment
                |             3 - For cylindrical environment

        :param int i_environment_type:
        :return: RenderingEnvironment
        :rtype: RenderingEnvironment
        """
        return RenderingEnvironment(self.rendering_environments.Add(i_environment_type))

    def item(self, i_index: cat_variant) -> RenderingEnvironment:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As RenderingEnvironment
                | 
                |     Returns an environment index in the environments
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the environment to retrieve in the collection of
                |             environments. Compared with other collections, you cannot use the name of the
                |             environment as argument. 
                | 
                |     Returns:
                |         The retrieved environment 
                | 
                | Example:
                |     The following example returns in MyEnvironment the sixth environment in a
                |     environment collection.
                | 
                |      Dim MyEnvironment As RenderingEnvironment
                |      Set MyEnvironment = RenderingEnvironments.Item(6)

        :param cat_variant i_index:
        :return: RenderingEnvironment
        :rtype: RenderingEnvironment
        """
        return RenderingEnvironment(self.rendering_environments.Item(i_index.com_object))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a environment from the environments collection.

        :param cat_variant i_index:
        :return: None
        :rtype: None
        """
        return self.rendering_environments.Remove(i_index.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(rendering_environments)
        # #     Dim iIndex (2)
        # #     rendering_environments.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_all(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveAll()
                | 
                |     Removes all environments.of the collection

        :return: None
        :rtype: None
        """
        return self.rendering_environments.RemoveAll()

    def __repr__(self):
        return f'RenderingEnvironments(name="{self.name}")'
