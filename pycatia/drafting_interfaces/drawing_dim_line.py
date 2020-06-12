#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class DrawingDimLine(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingDimLine
                | 
                | Manages dimension line of a dimension in drawing view.
                | 
                | This interface is obtained from DrawingDimension.GetDimLine
                | method.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drawing_dim_line = com_object

    @property
    def color(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Color() As long
                | 
                |     Returns or sets color of dimension line.
                | 
                |     Example:
                |         This example retrieves color of dimension line MyDimLine drawing
                |         dimension.
                | 
                |          oColorDimLine = MyDimLine.Color

        :return: int
        """

        return self.drawing_dim_line.Color

    @color.setter
    def color(self, value):
        """
        :param int value:
        """

        self.drawing_dim_line.Color = value

    @property
    def dim_line_graph_rep(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DimLineGraphRep() As CatDimLineGraphRep
                | 
                |     Returns or graphic representation of dimension line.
                | 
                |     Example:
                |         This example retrieves graphic representation of dimension line
                |         MyDimLine drawing dimension.
                | 
                |          odimLineGraphRep = MyDimLine.DimLineGraphRep

        :return: enum cat_dim_line_graph_rep
        """

        return self.drawing_dim_line.DimLineGraphRep

    @dim_line_graph_rep.setter
    def dim_line_graph_rep(self, value):
        """
        :param enum cat_dim_line_graph_rep value:
        """

        self.drawing_dim_line.DimLineGraphRep = value

    @property
    def dim_line_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DimLineOrientation() As CatDimOrientation
                | 
                |     Returns or orientation of dimension line.
                | 
                |     Example:
                |         This example retrieves orientation of dimension line MyDimLine drawing
                |         dimension.
                | 
                |          odimLineOrient = MyDimLine.DimLineOrientation

        :return: enum cat_dim_orientation
        """

        return self.drawing_dim_line.DimLineOrientation

    @dim_line_orientation.setter
    def dim_line_orientation(self, value):
        """
        :param enum cat_dim_orientation value:
        """

        self.drawing_dim_line.DimLineOrientation = value

    @property
    def dim_line_reference(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DimLineReference() As CatDimReference
                | 
                |     Returns or reference of dimension line.
                | 
                |     Example:
                |         This example retrieves reference of dimension line MyDimLine drawing
                |         dimension.
                | 
                |          odimLineRef = MyDimLine.DimLineReference

        :return: enum cat_dim_reference
        """

        return self.drawing_dim_line.DimLineReference

    @dim_line_reference.setter
    def dim_line_reference(self, value):
        """
        :param enum cat_dim_reference value:
        """

        self.drawing_dim_line.DimLineReference = value

    @property
    def dim_line_rep(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DimLineRep() As CatDimLineRep (Read Only)
                | 
                |     Returns or representation of dimension line.
                | 
                |     Example:
                |         This example retrieves representation of dimension line MyDimLine
                |         drawing dimension.
                | 
                |          odimLineRep = MyDimLine.DimLineRep

        :return: enum cat_dim_line_rep
        """

        return self.drawing_dim_line.DimLineRep

    @property
    def dim_line_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DimLineType() As long (Read Only)
                | 
                |     Returns type of dimension line.
                | 
                |     Example:
                |         This example retrieves type of dimension line MyDimLine drawing
                |         dimension.
                | 
                |          odimLineType = MyDimLine.DimLineType

        :return: int
        """

        return self.drawing_dim_line.DimLineType

    @property
    def thickness(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Thickness() As double
                | 
                |     Returns or sets thickness of dimension line.
                | 
                |     Example:
                |         This example retrieves thickness of dimension line MyDimLine drawing
                |         dimension.
                | 
                |          oThickDimLine = MyDimLine.Thickness

        :return: float
        """

        return self.drawing_dim_line.Thickness

    @thickness.setter
    def thickness(self, value):
        """
        :param float value:
        """

        self.drawing_dim_line.Thickness = value

    def get_dim_line_dir(self, o_dir_x, o_dir_y):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetDimLineDir(double oDirX,
                | double oDirY)
                | 
                |     Returns direction of a dimension line in case of a catDimUserDefined
                |     representation mode. To retrieve the representation mode:
                |     DrawingDimLine.get_DimLineRep.
                | 
                |     Parameters:
                | 
                |         oDirX,oDirY
                |             The components of the direction vector 
                |         Example:
                |             This example retrieves the direction vector of a dimension line
                |             MyDimLine drawing dimension.
                | 
                |              MyDimLine.GetDimLineDir oDirX, oDirY

        :param float o_dir_x:
        :param float o_dir_y:
        :return: None
        """
        return self.drawing_dim_line.GetDimLineDir(o_dir_x, o_dir_y)

    def get_geom_info(self, o_geom_infos):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetGeomInfo(CATSafeArrayVariant oGeomInfos)
                | 
                |     Get geometrical information of dimension line.
                | 
                |     Parameters:
                | 
                |         oGeomInfos
                |             geometrical information. 
                |         Example:
                |             This example gets geometrical information of MyDimLine
                |             path.
                | 
                |              MyDimLine.GetGeomInfo(oGeomInfos)

        :param tuple o_geom_infos:
        :return: None
        """
        return self.drawing_dim_line.GetGeomInfo(o_geom_infos)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_geom_info'
        # # vba_code = """
        # # Public Function get_geom_info(drawing_dim_line)
        # #     Dim oGeomInfos (2)
        # #     drawing_dim_line.GetGeomInfo oGeomInfos
        # #     get_geom_info = oGeomInfos
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_symb_color(self, index):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetSymbColor(long Index) As long
                | 
                |     Get symbol color of dimension line.
                | 
                |     Parameters:
                | 
                |         Index
                |             1:first symbol 2:second symbol 3:leader symbol 
                |         oColorSymb
                |             symbol color. 
                |         Example:
                |             This example gets symbol color of MyDimLine path.
                | 
                |              ColorSymb = MyDimLine.GetSymbColor(Index)

        :param int index:
        :return: int
        """
        return self.drawing_dim_line.GetSymbColor(index)

    def get_symb_thickness(self, index):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetSymbThickness(long Index) As double
                | 
                |     Get symbol thickness of dimension line.
                | 
                |     Parameters:
                | 
                |         Index
                |             1:first symbol 2:second symbol 3:leader symbol 
                |         oThickSymb
                |             symbol thickness. 
                |         Example:
                |             This example gets symbol thickness of MyDimLine
                |             path.
                | 
                |              ThickSymb = MyDimLine.GetSymbThickness(Index)

        :param int index:
        :return: float
        """
        return self.drawing_dim_line.GetSymbThickness(index)

    def get_symb_type(self, index):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetSymbType(long Index) As CatDimSymbols
                | 
                |     Get symbol type of dimension line.
                | 
                |     Parameters:
                | 
                |         Index
                |             1:first symbol 2:second symbol 3:leader symbol 
                |         oTypeSymb
                |             symbol type. 
                |         Example:
                |             This example gets symbol type of MyDimLine path.
                | 
                |              typeSymb = MyDimLine.GetSymbType(Index)

        :param int index:
        :return: enum cat_dim_symbols
        """
        return self.drawing_dim_line.GetSymbType(index)

    def set_symb_color(self, index, i_color_symb):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetSymbColor(long Index,
                | long iColorSymb)
                | 
                |     Set symbol color of dimension line.
                | 
                |     Parameters:
                | 
                |         Index
                |             1:first symbol 2:second symbol 3:leader symbol 
                |         oColorSymb
                |             symbol color. 
                |         Example:
                |             This example sets symbol color of MyDimLine path.
                | 
                |              MyDimLine.SetSymbColor(Index, iColorSymb)

        :param int index:
        :param int i_color_symb:
        :return: None
        """
        return self.drawing_dim_line.SetSymbColor(index, i_color_symb)

    def set_symb_thickness(self, index, i_thick_symb):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetSymbThickness(long Index,
                | double iThickSymb)
                | 
                |     Set symbol thickness of dimension line.
                | 
                |     Parameters:
                | 
                |         Index
                |             1:first symbol 2:second symbol 3:leader symbol 
                |         oThickSymb
                |             symbol thickness. 
                |         Example:
                |             This example sets symbol thickness of MyDimLine
                |             path.
                | 
                |              MyDimLine.GetSymbThickness(Index, iThickSymb)

        :param int index:
        :param float i_thick_symb:
        :return: None
        """
        return self.drawing_dim_line.SetSymbThickness(index, i_thick_symb)

    def set_symb_type(self, index, i_symb_type):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetSymbType(long Index,
                | CatDimSymbols iSymbType)
                | 
                |     Set symbol type of dimension line.
                | 
                |     Parameters:
                | 
                |         Index
                |             1:first symbol 2:second symbol 3:leader symbol 
                |         iSymbType
                |             symbol type. 
                |         Example:
                |             This example sets symbol type of MyDimLine path.
                | 
                |              MyDimLine.SetSymbType(Index, iSymbType)

        :param int index:
        :param CatDimSymbols i_symb_type:
        :return: None
        """
        return self.drawing_dim_line.SetSymbType(index, i_symb_type.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_symb_type'
        # # vba_code = """
        # # Public Function set_symb_type(drawing_dim_line)
        # #     Dim Index (2)
        # #     drawing_dim_line.SetSymbType Index
        # #     set_symb_type = Index
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DrawingDimLine(name="{self.name}")'
