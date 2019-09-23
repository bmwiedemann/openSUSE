#
# spec file for package python-epubmerge
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define upname EpubMerge
%define upnamedown epubmerge
%define skip_python3 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-epubmerge
Version:        2.3.0
Release:        0
Summary:        EpubMerge Calibre Plugin
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/JimmXinu/EpubMerge
Source:         https://github.com/JimmXinu/EpubMerge/archive/v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2
BuildArch:      noarch
%python_subpackages

%description
This plugin provides the ability to create new EPUBs by combining the contents
of existing (non-DRM) EPUB format eBooks.

Main Features of EpubMerge Plugin:
    - Select a list of stories in calibre,
    - Order them,
    - Edit the metadata for the new combined eBook, and then,
    - Merge the contents of the EPUBs together into the new eBook, now
      including cover from metadata if set.
    - UnMerge previously merged epubs if metadata was saved during merge.
    - Configurably able to save the metadata for each merged book for UnMerging
      later if desired. (Defaults to On.)
    - Configurably able to populate custom columns from source books.
    - Options now stored inside the Library rather than an external JSON file.
    - CLI

There are a few configurable options: whether or not to insert a Table of
Contents entry for each merged book (with it's original TOC nested underneath
it), an option to flatten the TOC down to one level only, and including the
merged books comments. These options are stored by Library.

%prep
%setup -q -n %{upname}-%{version}

%build
/bin/true

%install
install -p -D epubmerge.py %{buildroot}%{_bindir}/%{upnamedown}

%files %{python_files}
%license LICENSE
%doc README.md
%{_bindir}/%{upnamedown}

%changelog
