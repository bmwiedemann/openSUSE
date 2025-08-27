#
# spec file for package python-actdiag
#
# Copyright (c) 2025 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-actdiag
Version:        3.0.0
Release:        0
Summary:        Text to activity-diagram image generator
License:        Apache-2.0
URL:            http://blockdiag.com/
Source:         https://files.pythonhosted.org/packages/source/a/actdiag/actdiag-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#blockdiag/actdiag#25
Patch0:         clean-up-assertions.patch
# PATCH-FIX-OPENSUSE Support new fancy pytest parameterized methods in blockdiag
Patch1:         support-new-fancy-blockdiag-pytest.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module blockdiag >= 3}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-blockdiag >= 3
BuildArch:      noarch
%python_subpackages

%description
actdiag generates activity-diagram image files from spec-text files.

%prep
%autosetup -p1 -n actdiag-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/actdiag
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# All of these are shipped by blockdiag and fail to parse
donttest+="diagram_attributes.diag-svg-options or "
donttest+="edge_datamodels.diag-svg-options or "
donttest+="empty_group.diag-svg-options or "
donttest+="empty_group_declaration.diag-svg-options or "
donttest+="empty_nested_group.diag-svg-options or "
donttest+="group_and_skipped_edge.diag-svg-options or "
donttest+="group_attribute.diag-svg-options or "
donttest+="group_children_height.diag-svg-options or "
donttest+="group_children_order.diag-svg-options or "
donttest+="group_children_order2.diag-svg-options or "
donttest+="group_children_order3.diag-svg-options or "
donttest+="group_children_order4.diag-svg-options or "
donttest+="group_declare_as_node_attribute.diag-svg-options or "
donttest+="group_height.diag-svg-options or "
donttest+="group_id_and_node_id_are_not_conflicted.diag-svg-options or "
donttest+="group_label.diag-svg-options or "
donttest+="group_order.diag-svg-options or "
donttest+="group_order2.diag-svg-options or "
donttest+="group_order3.diag-svg-options or "
donttest+="group_orientation.diag-svg-options or "
donttest+="group_sibling.diag-svg-options or "
donttest+="group_works_node_decorator.diag-svg-options or "
donttest+="large_group_and_node.diag-svg-options or "
donttest+="large_group_and_node2.diag-svg-options or "
donttest+="large_group_and_two_nodes.diag-svg-options or "
donttest+="merge_groups.diag-svg-options or "
donttest+="multiple_groups.diag-svg-options or "
donttest+="multiple_nested_groups.diag-svg-options or "
donttest+="nested_group_orientation.diag-svg-options or "
donttest+="nested_group_orientation2.diag-svg-options or "
donttest+="nested_groups.diag-svg-options or "
donttest+="nested_groups_and_edges.diag-svg-options or "
donttest+="nested_groups_work_node_decorator.diag-svg-options or "
donttest+="node_attribute_and_group.diag-svg-options or "
donttest+="node_in_group_follows_outer_node.diag-svg-options or "
donttest+="node_link.diag-svg-options or "
donttest+="outer_node_follows_node_in_group.diag-svg-options or "
donttest+="reverse_multiple_groups.diag-svg-options or "
donttest+="separate1.diag-svg-options or "
donttest+="separate2.diag-svg-options or "
donttest+="simple_group.diag-svg-options"
%pytest src/actdiag/tests -k "not ($donttest)"

%pre
%python_libalternatives_reset_alternative actdiag

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/actdiag
%{python_sitelib}/actdiag
%{python_sitelib}/actdiag-%{version}.dist-info

%changelog
