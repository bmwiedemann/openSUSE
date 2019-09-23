#
# spec file for package python-coverage
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
Name:           python-coverage
Version:        4.5.4
Release:        0
Summary:        Code coverage measurement for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/nedbat/coveragepy
Source:         https://files.pythonhosted.org/packages/source/c/coverage/coverage-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module unittest-mixins}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires:       python-xml
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Coverage.py measures code coverage, typically during test execution. It uses
the code analysis tools and tracing hooks provided in the Python standard
library to determine which lines are executable, and which have been executed.

%prep
%setup -q -n coverage-%{version}
# do not require xdist
sed -i -e '/addopts/d' setup.cfg
# writes in /usr/
rm tests/test_process.py
# summary differs trivialy
rm tests/test_summary.py
# requires additional plugins
rm tests/test_plugins.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/coverage
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%if 0%{?have_python2} && ! 0%{?skip_python2}
ln -sf coverage-%{python2_version} %{buildroot}%{_bindir}/coverage2
%endif
%if 0%{?have_python3} && ! 0%{?skip_python3}
ln -sf coverage-%{python3_version} %{buildroot}%{_bindir}/coverage3
%endif

%check
# GetZipBytesTest.test_get_encoded_zip_files - needs zip command
# test_egg - needs generated egg file
# test_doctest - weird doctest importing 
# test_unicode - differs between py2/py3
# test_version - checks for non-compiled variant, we ship only compiled one
# test_multiprocessing_with_branching - whitespace issue in regexp
# test_farm - tries to write in /usr
# test_dothtml_not_python - no idea
# test_bytes
# test_one_of
export LANG=en_US.UTF8
# Copy executables to py2/3 build areas, to be used for testing
%{python_expand mkdir build/bin
for filepath in %{buildroot}/%{_bindir}/coverage*-%{$python_bin_suffix}; do
  filename=$(basename $filepath)
  unsuffixed=${filename/-%{$python_bin_suffix}/}
  cp $filepath build/bin/$unsuffixed
done
export PATH="$(pwd)/build/bin:$PATH"
export PYTHONPATH=%{buildroot}%{$python_sitearch}
py.test-%{$python_bin_suffix} -v -k 'not (test_get_encoded_zip_files or test_egg or test_doctest or test_unicode or test_version or test_multiprocessing_with_branching or test_farm or test_dothtml_not_python or test_one_of or test_bytes)'
rm -r build/bin
}

%post
%python_install_alternative coverage

%postun
%python_uninstall_alternative coverage

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst CONTRIBUTORS.txt README.rst TODO.txt howto.txt
%python_alternative %{_bindir}/coverage
%python2_only %{_bindir}/coverage2
%python3_only %{_bindir}/coverage3
%{python_sitearch}/coverage/
%{python_sitearch}/coverage-%{version}-py%{python_version}.egg-info

%changelog
