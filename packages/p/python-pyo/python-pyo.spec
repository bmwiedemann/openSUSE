#
# spec file for package python-pyo
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-pyo
Version:        1.0.5
Release:        0
Summary:        Python digital signal processing module
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://ajaxsoundstudio.com/software/pyo/
Source:         https://files.pythonhosted.org/packages/source/p/pyo/pyo-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/belangeo/pyo/master/LICENSE
# PATCH-FIX-UPSTREAM - Fix multiple incorrect declarations and signatures of callback functions
Patch:          https://github.com/belangeo/pyo/pull/277.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  portmidi-devel
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(sndfile)
# Test build requires, aifc is no longer part of python standard lib
# since python3.13:
# https://github.com/belangeo/pyo/issues/286
BuildRequires:  python313-standard-aifc
Requires:       (python-standard-aifc if python-base >= 3.13)
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
PYO is a Python module written in C to help digital signal processing
script creation.

%prep
%setup -q -n pyo-%{version}
%autopatch -p1
cp %{SOURCE1} .

%build
export CFLAGS="%{optflags}"
%{pyproject_wheel -C "--build-option=--use-jack" -C "--build-option=--use-double" .}

%install
%pyproject_install

# Fix non-executable-script editor and examples
%{python_expand #
for i in editor examples/algorithmic examples/sequencing examples/matrix examples/fft examples/sampling examples/synthesis
do
sed -i "/^#!\s*\/usr\/bin\/env python/d" %{buildroot}%{$python_sitearch}/pyo/$i/*.py
done
}

%python_clone -a %{buildroot}%{_bindir}/epyo
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Change directory to avoid importing from source
mkdir -p test
pushd test
# testsuite is broken and can not be run even from github tarball
%{python_expand #
PYTHONPATH=%{buildroot}%{$python_sitearch} $python -c "import pyo; print(pyo.PYO_VERSION)"
}
popd

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative epyo

%post
%python_install_alternative epyo

%postun
%python_uninstall_alternative epyo

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/epyo
%{python_sitearch}/pyo
%{python_sitearch}/pyo64
%{python_sitearch}/pyo-%{version}*-info

%changelog
