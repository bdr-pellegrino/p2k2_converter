from p2k2_converter.core.workflow.workflow_strategy import WorkflowStrategy
from p2k2_converter.core.workflow.workflow import Workflow
from p2k2_converter.core.workflow.close import Close
from p2k2_converter.core.workflow.moderna import Moderna
from p2k2_converter.core.workflow.modx import Modx
from p2k2_converter.core.workflow.modu import Modu
from p2k2_converter.core.workflow.modi import Modi
from p2k2_converter.core.workflow.full_d import FullD
from p2k2_converter.core.workflow.full_w import FullW
from p2k2_converter.core.workflow.full_g import FullG
from p2k2_converter.core.workflow.gate import Gate
from p2k2_converter.core.workflow.click_rapid import ClickRapid
from p2k2_converter.core.utils import Sentence


__class_names__ = {Close, Moderna, ClickRapid, Modu, Modi, FullD, FullW, FullG, Gate}


def workflow_for_product(product_name: str, *args, **kwargs) -> WorkflowStrategy:
    """
    This function will return the correct workflow for the product name given.
    Args:
        product_name: Name of the product to get the workflow for
        *args:
        **kwargs:

    Returns:
        The workflow for the product name given
    """
    for workflow_class in __class_names__:
        name = Sentence(product_name.lower()).pascal_case()
        class_name = Sentence(workflow_class.__name__).pascal_case()
        if name == class_name:
            return workflow_class(*args, **kwargs)


__all__ = [
    "WorkflowStrategy",
    "Workflow",
    "Close",
    "Moderna",
    "ClickRapid",
    "workflow_for_product",
    "Modx",
    "Modu",
    "Modi",
    "FullD",
    "FullW",
    "FullG",
    "Gate"
]
