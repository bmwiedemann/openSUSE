#
# spec file for package analyzeMFT
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           analyzeMFT
Version:        2.0.4
Release:        0
Summary:        A Python tool to deconstruct the Windows NTFS $MFT file
License:        CPL-1.0
Group:          Development/Libraries/Python
Url:            https://github.com/dkovar/analyzeMFT
Source:         https://github.com/dkovar/analyzeMFT/archive/v2.0.4.tar.gz
BuildRequires:  python-devel
Requires:       python
Requires:       python-tk
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
analyzeMFT.py is designed to fully parse the MFT file from an NTFS filesystem and present the results as accurately as possible in a format that allows further analysis with other tools. At present, it parses the attributes from a $MFT file to produce the following output:

    Record Number
    Good - if the entry is valid
    Active - if the entry is active
    Record type - the type of record
    Record Sequence - the sequence number for the record
    Parent Folder Record Number
    Parent Folder Sequence Number
    For the standard information attribute:
        Creation date
        Modification date
        Access date
        Entry date
    For up to four file name records:
        File name
        Creation date
        Modification date
        Access date
        Entry date
        Object ID
        Birth Volume ID
        Birth Object ID
        Birth Domain ID
    And flags to show if each of the following attributes is present:
        Standard Information, Attribute List, Filename, Object ID, Volume Name, Volume Info, Data, Index Root, Index Allocation, Bitmap, Reparse Point, EA Information, EA, Property Set, Logged Utility Stream
    Notes/Log - Field used to log any significant events or observations relating to this record
        std-fn-shift - Populated if anomaly detection is turned on. Y/N. Y indicates that the FN create date is later than the STD create date.
        usec-zero - Populated if anomaly detection is turned on. Y/N. Y indicates that the STD create date's microsecond value is zero.

For each entry in the MFT a record is written to an output file in CSV format.

Major contributions from Matt Sabourin.

%prep
%setup -q

%build

%install
python setup.py install --root=%{buildroot} --prefix=%{_prefix}

%files
%defattr(-,root,root)
%doc CHANGES.txt LICENSE.txt README.txt
%{_bindir}/analyzeMFT.py
%{python_sitelib}/analyzeMFT-%{version}-py2.7.egg-info
%attr(644,root,root) %{python_sitelib}/analyzemft

%changelog
