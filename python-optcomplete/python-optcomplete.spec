#
# spec file for package python-optcomplete
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{!?license: %global license %doc}
%define modname optcomplete
%define unmangled_version 1.2-devel
Name:           python-optcomplete
Version:        1.2_devel
Release:        0
Summary:        Automatic Shell Completion Support for Scripts Using Optparse
License:        BSD-3-Clause
Group:          Development/Libraries/Python
Url:            http://furius.ca/optcomplete
Source0:        %{modname}-%{unmangled_version}.tar.bz2
Patch1:         optcomplete-1.2-devel-fix-shebang.patch
BuildRequires:  python-devel
%py_requires
BuildArch:      noarch

%description
This module provide automatic bash completion support for programs that use the
optparse module.  The premise is that the optparse options parser specifies
enough information (and more) for us to be able to generate completion strings
esily.  Another advantage of this over traditional completion schemes where the
completion strings are hard-coded in a separate bash source file, is that the
same code that parses the options is used to generate the completions, so the
completions is always up-to-date with the program itself.

In addition, we allow you specify a list of regular expressions or code that
define what kinds of files should be proposed as completions to this file if
needed.  If you want to implement more complex behaviour, you can instead
specify a function, which will be called with the current directory as an
argument.

You need to activate bash completion using the shell script function that comes
with optcomplete (see http://furius.ca/optcomplete for more details).

%prep
%setup -q -n %{modname}-%{unmangled_version}
%patch1 -p1
sed -i '1s/^#!\/usr\/bin\/env python$/#!\/usr\/bin\/python2/' bin/*

%build
python setup.py build

%install
python setup.py install \
  --root=%{buildroot} \
  --prefix=%{_prefix} \
  --record=%{name}.files
mv bin example
chmod -x example/*
mkdir bash_completion
mv etc/bashrc etc/env etc/optcomplete.zsh bash_completion/
chmod -x bash_completion/optcomplete.zsh
install -Dm 664 etc/optcomplete.bash %{buildroot}%{_sysconfdir}/bash_completion.d/optcomplete.sh

%files -f %{name}.files
%config %{_sysconfdir}/bash_completion.d/*
%doc README TODO VERSION CHANGES CREDITS
%license COPYING
%doc doc/* example bash_completion

%changelog
