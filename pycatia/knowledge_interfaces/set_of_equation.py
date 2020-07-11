#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.relation import Relation


class SetOfEquation(Relation):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.KnowledgeObject
                |                        KnowledgeInterfaces.KnowledgeActivateObject
                |                             KnowledgeInterfaces.Relation
                |                                 SetOfEquation
                | 
                | Represents the set of equations object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.set_of_equation = com_object

    def get_max_calculation_time(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetMaxCalculationTime() As long
                | 
                |     Returns the maximum time of the model calculations.

        :return: int
        :rtype: int
        """
        return self.set_of_equation.GetMaxCalculationTime()

    def get_precision(self) -> float:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPrecision() As double
                | 
                |     Returns the calculation precision.

        :return: float
        :rtype: float
        """
        return self.set_of_equation.GetPrecision()

    def get_symbolc_transformations(self) -> bool:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetSymbolcTransformations() As boolean
                | 
                |     Returns whether the Gauss method is used during the symbolic
                |     transformation.
                |     TRUE if the Gauss method is used during the symbolic transformation.

        :return: bool
        :rtype: bool
        """
        return self.set_of_equation.GetSymbolcTransformations()

    def is_stop_dialog(self) -> bool:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func IsStopDialog() As boolean
                | 
                |     Returns whether the "Stop Dialog" will be shown during
                |     calculations.
                |     TRUE if the 'Stop Dialog' will be shown during calculations.

        :return: bool
        :rtype: bool
        """
        return self.set_of_equation.IsStopDialog()

    def set_max_calculation_time(self, i_max_time: int) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetMaxCalculationTime(long iMaxTime)
                | 
                |     Sets a maximum time to the model calculations.

        :param int i_max_time:
        :return: None
        :rtype: None
        """
        return self.set_of_equation.SetMaxCalculationTime(i_max_time)

    def set_parameter_as_input(self, i_parameter: Parameter) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetParameterAsInput(Parameter iParameter)
                | 
                |     Specifies that the parameter must be considered as input
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iParameter
                |             The parameter to set up as input of the
                |             SetOfEquationObject

        :param Parameter i_parameter:
        :return: None
        :rtype: None
        """
        return self.set_of_equation.SetParameterAsInput(i_parameter.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_parameter_as_input'
        # # vba_code = """
        # # Public Function set_parameter_as_input(set_of_equation)
        # #     Dim iParameter (2)
        # #     set_of_equation.SetParameterAsInput iParameter
        # #     set_parameter_as_input = iParameter
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_parameter_as_output(self, i_parameter: Parameter) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetParameterAsOutput(Parameter iParameter)
                | 
                |     Specifies that the parameter must be considered as an output
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iParameter
                |             The parameter to set up as output of the
                |             SetOfEquationObject

        :param Parameter i_parameter:
        :return: None
        :rtype: None
        """
        return self.set_of_equation.SetParameterAsOutput(i_parameter.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_parameter_as_output'
        # # vba_code = """
        # # Public Function set_parameter_as_output(set_of_equation)
        # #     Dim iParameter (2)
        # #     set_of_equation.SetParameterAsOutput iParameter
        # #     set_parameter_as_output = iParameter
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_precision(self, i_eps: float) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPrecision(double iEps)
                | 
                |     Sets the calculation precision.
                | 
                |     Parameters:
                | 
                |         iEps
                |             a precision
                |             Legal values: 1e-10 ≤ iEps ≤ 0.1

        :param float i_eps:
        :return: None
        :rtype: None
        """
        return self.set_of_equation.SetPrecision(i_eps)

    def use_stop_dialog(self, i_used: bool) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub UseStopDialog(boolean iUsed)
                | 
                |     Specifies whether the 'Stop Dialog' should be shown during
                |     calculations.
                |     TRUE to show the 'Stop Dialog' during calculations.

        :param bool i_used:
        :return: None
        :rtype: None
        """
        return self.set_of_equation.UseStopDialog(i_used)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'use_stop_dialog'
        # # vba_code = """
        # # Public Function use_stop_dialog(set_of_equation)
        # #     Dim iUsed (2)
        # #     set_of_equation.UseStopDialog iUsed
        # #     use_stop_dialog = iUsed
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def use_symbolc_transformations(self, i_gauss: bool) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub UseSymbolcTransformations(boolean iGauss)
                | 
                |     Specifies whether the Gauss method should be used during the symbolic
                |     transformation.
                |     TRUE to use the Gauss method during the symbolic transformation.

        :param bool i_gauss:
        :return: None
        :rtype: None
        """
        return self.set_of_equation.UseSymbolcTransformations(i_gauss)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'use_symbolc_transformations'
        # # vba_code = """
        # # Public Function use_symbolc_transformations(set_of_equation)
        # #     Dim iGauss (2)
        # #     set_of_equation.UseSymbolcTransformations iGauss
        # #     use_symbolc_transformations = iGauss
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SetOfEquation(name="{ self.name }")'
