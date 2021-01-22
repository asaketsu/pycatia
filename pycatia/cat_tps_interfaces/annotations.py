#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection
from pycatia.cat_tps_interfaces.annotation import Annotation
from pycatia.types import cat_variant


class Annotations(Collection):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Annotations
                | 
                | Interface for collection of TPS objects CATIAAnnotation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotations = com_object
        self.child_object = Annotation

    def add(self, i_annot: Annotation) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Add(Annotation iAnnot)
                | 
                |     Add an Annotation.

        :param Annotation i_annot:
        :return: None
        :rtype: None
        """
        return self.annotations.Add(i_annot.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add'
        # # vba_code = """
        # # Public Function add(annotations)
        # #     Dim iAnnot (2)
        # #     annotations.Add iAnnot
        # #     add = iAnnot
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def item(self, i_index: cat_variant) -> Annotation:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Annotation
                | 
                |     Retrieves an Annotation managing by CATIAAnnotation. Deprecated method:
                |     Item method is replaced by Item2 has.

        :param CATVariant i_index:
        :return: Annotation
        :rtype: Annotation
        """
        return Annotation(self.annotations.Item(i_index))

    def item2(self, i_index: cat_variant) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item2(CATVariant iIndex) As AnyObject
                | 
                |     Retrieve an Annotation using interface CATIAAnnotation2

        :param CATVariant i_index:
        :return: AnyObject
        :rtype: AnyObject
        """
        return AnyObject(self.annotations.Item2(i_index.com_object))

    def __repr__(self):
        return f'Annotations(name="{ self.name }")'
