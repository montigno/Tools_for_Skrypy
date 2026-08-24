class cmtk_AverageNetworks:
    """
    Note:
        dependencies: Nipype,cmtk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.cmtk.nx import AverageNetworks
        at = AverageNetworks()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def gpickled_groupavg(self) -> None:
        return self.res.outputs.gpickled_groupavg

    def gexf_groupavg(self) -> None:
        return self.res.outputs.gexf_groupavg

    def matlab_groupavgs(self) -> list[None]:
        return self.res.outputs.matlab_groupavgs

###############################################################################


class cmtk_CFFConverter:
    """
    Note:
        dependencies: Nipype,cmtk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.cmtk.convert import CFFConverter
        at = CFFConverter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def connectome_file(self) -> None:
        return self.res.outputs.connectome_file

###############################################################################


class cmtk_CreateMatrix:
    """
    Note:
        dependencies: Nipype,cmtk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, roi_file="path", tract_file="path", resolution_network_file="path", **options):
        from nipype.interfaces.cmtk.cmtk import CreateMatrix
        at = CreateMatrix()
        at.inputs.roi_file = roi_file
        at.inputs.tract_file = tract_file
        at.inputs.resolution_network_file = resolution_network_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def matrix_file(self) -> None:
        return self.res.outputs.matrix_file

    def intersection_matrix_file(self) -> None:
        return self.res.outputs.intersection_matrix_file

    def matrix_files(self) -> list[None]:
        return self.res.outputs.matrix_files

    def matlab_matrix_files(self) -> list[None]:
        return self.res.outputs.matlab_matrix_files

    def matrix_mat_file(self) -> None:
        return self.res.outputs.matrix_mat_file

    def intersection_matrix_mat_file(self) -> None:
        return self.res.outputs.intersection_matrix_mat_file

    def mean_fiber_length_matrix_mat_file(self) -> None:
        return self.res.outputs.mean_fiber_length_matrix_mat_file

    def median_fiber_length_matrix_mat_file(self) -> None:
        return self.res.outputs.median_fiber_length_matrix_mat_file

    def fiber_length_std_matrix_mat_file(self) -> None:
        return self.res.outputs.fiber_length_std_matrix_mat_file

    def endpoint_file(self) -> None:
        return self.res.outputs.endpoint_file

    def endpoint_file_mm(self) -> None:
        return self.res.outputs.endpoint_file_mm

    def fiber_length_file(self) -> None:
        return self.res.outputs.fiber_length_file

    def fiber_label_file(self) -> None:
        return self.res.outputs.fiber_label_file

    def fiber_labels_noorphans(self) -> None:
        return self.res.outputs.fiber_labels_noorphans

    def filtered_tractography(self) -> None:
        return self.res.outputs.filtered_tractography

    def filtered_tractography_by_intersections(self) -> None:
        return self.res.outputs.filtered_tractography_by_intersections

    def filtered_tractographies(self) -> list[None]:
        return self.res.outputs.filtered_tractographies

    def stats_file(self) -> None:
        return self.res.outputs.stats_file

###############################################################################


class cmtk_CreateNodes:
    """
    Note:
        dependencies: Nipype,cmtk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, roi_file="path", resolution_network_file="path", **options):
        from nipype.interfaces.cmtk.cmtk import CreateNodes
        at = CreateNodes()
        at.inputs.roi_file = roi_file
        at.inputs.resolution_network_file = resolution_network_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def node_network(self) -> None:
        return self.res.outputs.node_network

###############################################################################


class cmtk_MergeCNetworks:
    """
    Note:
        dependencies: Nipype,cmtk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.cmtk.convert import MergeCNetworks
        at = MergeCNetworks()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def connectome_file(self) -> None:
        return self.res.outputs.connectome_file

###############################################################################


class cmtk_NetworkBasedStatistic:
    """
    Note:
        dependencies: Nipype,cmtk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_group1=["path"], in_group2=["path"], **options):
        from nipype.interfaces.cmtk.nbs import NetworkBasedStatistic
        at = NetworkBasedStatistic()
        at.inputs.in_group1 = in_group1
        at.inputs.in_group2 = in_group2
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def nbs_network(self) -> None:
        return self.res.outputs.nbs_network

    def nbs_pval_network(self) -> None:
        return self.res.outputs.nbs_pval_network

    def network_files(self) -> list[None]:
        return self.res.outputs.network_files

###############################################################################


class cmtk_NetworkXMetrics:
    """
    Note:
        dependencies: Nipype,cmtk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.cmtk.nx import NetworkXMetrics
        at = NetworkXMetrics()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def gpickled_network_files(self) -> list[None]:
        return self.res.outputs.gpickled_network_files

    def matlab_matrix_files(self) -> list[None]:
        return self.res.outputs.matlab_matrix_files

    def global_measures_matlab(self) -> None:
        return self.res.outputs.global_measures_matlab

    def node_measures_matlab(self) -> None:
        return self.res.outputs.node_measures_matlab

    def edge_measures_matlab(self) -> None:
        return self.res.outputs.edge_measures_matlab

    def node_measure_networks(self) -> list[None]:
        return self.res.outputs.node_measure_networks

    def edge_measure_networks(self) -> list[None]:
        return self.res.outputs.edge_measure_networks

    def k_networks(self) -> list[None]:
        return self.res.outputs.k_networks

    def k_core(self) -> None:
        return self.res.outputs.k_core

    def k_shell(self) -> None:
        return self.res.outputs.k_shell

    def k_crust(self) -> None:
        return self.res.outputs.k_crust

    def pickled_extra_measures(self) -> None:
        return self.res.outputs.pickled_extra_measures

    def matlab_dict_measures(self) -> list[None]:
        return self.res.outputs.matlab_dict_measures

###############################################################################


class cmtk_Parcellate:
    """
    Note:
        dependencies: Nipype,cmtk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, subject_id='', **options):
        from nipype.interfaces.cmtk.parcellation import Parcellate
        at = Parcellate()
        at.inputs.subject_id = subject_id
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def roi_file(self) -> None:
        return self.res.outputs.roi_file

    def roiv_file(self) -> None:
        return self.res.outputs.roiv_file

    def white_matter_mask_file(self) -> None:
        return self.res.outputs.white_matter_mask_file

    def cc_unknown_file(self) -> None:
        return self.res.outputs.cc_unknown_file

    def ribbon_file(self) -> None:
        return self.res.outputs.ribbon_file

    def aseg_file(self) -> None:
        return self.res.outputs.aseg_file

    def roi_file_in_structural_space(self) -> None:
        return self.res.outputs.roi_file_in_structural_space

    def dilated_roi_file_in_structural_space(self) -> None:
        return self.res.outputs.dilated_roi_file_in_structural_space

###############################################################################


class cmtk_ROIGen:
    """
    Note:
        dependencies: Nipype,cmtk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, aparc_aseg_file="path", **options):
        from nipype.interfaces.cmtk.cmtk import ROIGen
        at = ROIGen()
        at.inputs.aparc_aseg_file = aparc_aseg_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def roi_file(self) -> None:
        return self.res.outputs.roi_file

    def dict_file(self) -> None:
        return self.res.outputs.dict_file

###############################################################################


