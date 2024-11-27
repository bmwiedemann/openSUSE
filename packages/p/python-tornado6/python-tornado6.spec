#
# spec file for package python-tornado6
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


%{?sle15_python_module_pythons}
Name:           python-tornado6
Version:        6.4.2
Release:        0
Summary:        Open source version of scalable, non-blocking web server that power FriendFeed
License:        Apache-2.0
URL:            https://www.tornadoweb.org
Source:         https://files.pythonhosted.org/packages/source/t/tornado/tornado-%{version}.tar.gz
Source99:       python-tornado6-rpmlintrc
# PATCH-FIX-OPENSUSE ignore-resourcewarning-doctests.patch -- ignore resource warnings on OBS
Patch0:         ignore-resourcewarning-doctests.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pycares}
BuildRequires:  %{python_module pycurl}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Recommends:     python-Twisted
Recommends:     python-pycares
Recommends:     python-pycurl
Recommends:     python-service_identity
Conflicts:      python-tornado-impl
Provides:       python-tornado = %{version}
Provides:       python-tornado-impl = %{version}
Provides:       python-toro = %{version}
Obsoletes:      python-toro < %{version}
%python_subpackages

%description
Tornado is an open source version of the scalable, non-blocking web server and
tools that power FriendFeed. The FriendFeed application is written using a web
framework that looks a bit like web.py or Google's webapp, but with additional
tools and optimizations to take advantage of the underlying non-blocking
infrastructure.

The framework is distinct from most mainstream web server frameworks (and
certainly most Python frameworks) because it is non-blocking and reasonably
fast. Because it is non-blocking and uses epoll, it can handle thousands of
simultaneous standing connections, which means it is ideal for real-time web
services. We built the web server specifically to handle FriendFeed's real-time
features — every active user of FriendFeed maintains an open connection to the
FriendFeed servers. (For more information on scaling servers to support
thousands of clients, see The C10K problem.)

%prep
%autosetup -p1 -n tornado-%{version}
# Fix non-executable script rpmlint issue:
find tornado -name "*.py" -exec sed -i "/#\!\/usr\/bin\/.*/d" {} \;

%pre
# remove egg-info _file_, being replaced by an egg-info directory
if [ -f %{python_sitearch}/tornado-%{version}-py%{python_version}.egg-info ]; then
    rm %{python_sitearch}/tornado-%{version}-py%{python_version}.egg-info
fi

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand #
# do not install tests
rm -r %{buildroot}%{$python_sitearch}/tornado/test
# deduplicate files in python platlibdir
%fdupes %{buildroot}%{$python_sitearch}
# install demos into docdir and deduplicate
pdocdir=%{buildroot}%{_docdir}/$python-tornado6
mkdir -p ${pdocdir}
find ${pdocdir} -name "*.py" -exec sed -i "1{s|^#!.*$|%{_bindir}/$python|}" {} \;
find ${pdocdir} -type f -exec chmod a-x {} \;
%fdupes ${pdocdir}
}

%check
export ASYNC_TEST_TIMEOUT=30
export PYTHONDONTWRITEBYTECODE=1
export TRAVIS=1
%python_exec -m tornado.test.runtests --verbose

%files %{python_files}
%license LICENSE
%doc %{_docdir}/%{python_prefix}-tornado6
%{python_sitearch}/tornado
%{python_sitearch}/tornado-%{version}.dist-info

%changelog
