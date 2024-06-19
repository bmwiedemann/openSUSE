#
# spec file for package python-aubio
#
# Copyright (c) 2024 SUSE LLC
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


%define         skip_python36 1
Name:           python-aubio
Version:        0.4.9
Release:        0
Summary:        A collection of tools for music analysis
License:        GPL-3.0-or-later
URL:            http://aubio.org/
Source:         http://aubio.org/pub/aubio-%{version}.tar.bz2
Source1:        http://aubio.org/pub/aubio-%{version}.tar.bz2.asc
# PATCH-FIX-UPSTREAM waflib_python312.patch gh#aubio/aubio#394
# https://gitlab.com/ita1024/waf/-/commit/d2060dfd8af4edb5824153ff24e207b39ecd67a2
Patch1:         waflib_python312.patch
# PATCH-FIX-UPSTREAM 95ff046c.patch
# https://github.com/aubio/aubio/commit/95ff046c698156f21e2ca0d1d8a02c23ab76969f
Patch2:         95ff046c.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
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
%autosetup -p 1 -n aubio-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}/%{$python_sitearch}
%python_clone -a %{buildroot}/%{_bindir}/aubio
%python_clone -a %{buildroot}/%{_bindir}/aubiocut

%{python_expand # Remove shebang from non executable scripts
find %{buildroot}/%{$python_sitearch} -type f -name "*.py" -exec sed -i "1{/#!.*python/d}" {} \;
}

%check
# the two tests fail on 32bit due to precision issue
%pytest_arch -k 'not (test_meltohz or test_hztomel)'

%post
%{python_install_alternative aubio aubiocut}

%postun
%python_uninstall_alternative aubio

%files %{python_files}
%license COPYING
%doc README.md ChangeLog AUTHORS
%python_alternative %{_bindir}/aubio
%python_alternative %{_bindir}/aubiocut
%{python_sitearch}/aubio
%{python_sitearch}/aubio-%{version}*-info

%changelog
