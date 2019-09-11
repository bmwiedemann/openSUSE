# spec file for package suse-bug-reporter
#
# Copyright (c) 2011 Mihnea Dobrescu-Balaur <mihneadb@gmail.com>
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

Name:           bugreporter
Version:        1.0
Release:        0
License:        GPL-2.0+
Summary:        Bug reporting tool for openSUSE
Url:            https://github.com/mihneadb/suse_bug_reporter/
Group:          Development/Tools/Other
Source:         bugreporter-1.0.tar.gz
BuildRequires:  python >= 2.7
BuildArch:      noarch
Requires:       osc, python-bugzilla >= 0.6.2, bash-completion
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{py_requires}
 
%description
This is a bug reporting tool for openSUSE users. It can be used to
submit and query bug reports from Novell's Bugzilla.
 
%prep
%setup -q

%build
%{__python} setup.py build
 
%install
%{__python} setup.py install \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    --record-rpm=INSTALLED_FILES
sed -i 's#%{_mandir}/man1/bugreporter.1#%{_mandir}/man1/bugreporter.1.gz#' INSTALLED_FILES


%clean
rm -rf %{buildroot}
 
%files -f INSTALLED_FILES
%defattr(-,root,root)
%config (noreplace) %{_sysconfdir}/bash_completion.d/bugreporter
%changelog
