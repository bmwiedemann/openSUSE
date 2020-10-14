#
# spec file for package aspell-en
#
# Copyright (c) 2020 SUSE LLC
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


%define aspell_dict_dir %(aspell dump config dict-dir)
%define aspell_data_dir %(aspell dump config data-dir)

Name:           aspell-en
Version:        2019.10.06
Release:        0
Summary:        English Dictionaries for ASpell
License:        MIT AND BSD-3-Clause
Group:          Productivity/Text/Spell

URL:            http://wordlist.aspell.net/
Source0:        ftp://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-%{version}-0.tar.bz2
Source1:        ftp://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-%{version}-0.tar.bz2.sig
# keyring from ftp://ftp.gnu.org/gnu/aspell/dict/0index.html
#   http://aspell.net/dict-upload-key.txt + http://kevin.atkinson.dhs.org/public-key.txt
Source2:        aspell-en.keyring

BuildRequires:  aspell >= 0.60
BuildRequires:  fdupes
Provides:       locale(aspell:en)

%description
An English, Canadian English and British English dictionary for the ASpell
spell checker.

%prep
%setup -q -n aspell6-en-%{version}-0

%build
#not autoconf
./configure
make %{?_smp_mflags}

%install
%makeinstall
fdupes %{buildroot}%{aspell_dict_dir}

%files
%license Copyright
%doc README doc/ChangeLog doc/SCOWL-README doc/extra.txt
%{aspell_dict_dir}/*.rws
%{aspell_dict_dir}/*.multi
%{aspell_dict_dir}/*.alias
%{aspell_data_dir}/*.dat

%changelog
