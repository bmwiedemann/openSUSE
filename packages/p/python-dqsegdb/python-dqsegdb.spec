#
# spec file for package python-dqsegdb
#
# Copyright (c) 2025 SUSE LLC
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


%define skip_python2 1
%define modname dqsegdb
Name:           python-dqsegdb
Version:        2.1.0
Release:        0
Summary:        Client library for DQSegDB
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://git.ligo.org/computing/dqsegdb/client
Source:         https://files.pythonhosted.org/packages/source/d/dqsegdb/dqsegdb-%{version}.tar.gz
# PATCH-FIX-OPENSUSE remove-six.patch to remove dependency on python-six
Patch0:         remove-six.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 8.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-gpstime
Requires:       python-gwdatafind
Requires:       python-lal
Requires:       python-ligo-segments
Requires:       python-lscsoft-glue >= 3.0.1
Requires:       python-pyOpenSSL
Requires:       python-pyRXP
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION For tests
BuildRequires:  %{python_module lal}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest}
# /SECTION
ExcludeArch:    %{ix86}

%python_subpackages

%description
python-dqsegdb provides the python bindings and the client tools to
connect to LIGO/VIRGO DQSEGDB server instances.

%prep
%autosetup -p1 -n dqsegdb-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
for exe in ligolw_dq_query_dqsegdb ligolw_publish_threaded_dqxml_dqsegdb ligolw_segment_insert_dqsegdb ligolw_segment_query_dqsegdb ligolw_segments_from_cats_dqsegdb
do
%python_clone -a %{buildroot}%{_bindir}/${exe}
done

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative ligolw_dq_query_dqsegdb ligolw_publish_threaded_dqxml_dqsegdb ligolw_segment_insert_dqsegdb ligolw_segment_query_dqsegdb ligolw_segments_from_cats_dqsegdb

%postun
%python_uninstall_alternative ligolw_dq_query_dqsegdb ligolw_publish_threaded_dqxml_dqsegdb ligolw_segment_insert_dqsegdb ligolw_segment_query_dqsegdb ligolw_segments_from_cats_dqsegdb

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/ligolw_dq_query_dqsegdb
%python_alternative %{_bindir}/ligolw_publish_threaded_dqxml_dqsegdb
%python_alternative %{_bindir}/ligolw_segment_insert_dqsegdb
%python_alternative %{_bindir}/ligolw_segment_query_dqsegdb
%python_alternative %{_bindir}/ligolw_segments_from_cats_dqsegdb
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}.dist-info

%changelog
