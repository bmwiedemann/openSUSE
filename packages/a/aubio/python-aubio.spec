#
# spec file for package python-aubio
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-aubio
Version:        0.4.9
Release:        0
Summary:        A collection of tools for music analysis
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://aubio.org/
Source:         http://aubio.org/pub/aubio-%{version}.tar.bz2
Source1:        http://aubio.org/pub/aubio-%{version}.tar.bz2.asc
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module nose2}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
A python module to access the aubio library functions.

aubio is a library to label music and sounds. It listens to audio signals and attempts to detect events. For instance, when a drum is hit, at which frequency is a note, or at what tempo is a rhythmic melody.

Its features include segmenting a sound file before each of its attacks, performing pitch detection, tapping the beat and producing midi streams from live audio.

%prep
%setup -q -n aubio-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}/%{_bindir}/aubio
%python_clone -a %{buildroot}/%{_bindir}/aubiocut

%check
%ifpython3
export PYTHONPATH=%{buildroot}/%{python_sitearch}
%python_exec setup.py test
%endif

%post
%python_install_alternative aubio

%postun
%python_uninstall_alternative aubio

%files %{python_files}
%license COPYING
%doc README.md ChangeLog AUTHORS
%python_alternative %{_bindir}/aubio
%python_alternative %{_bindir}/aubiocut
%{python_sitearch}/*

%changelog
