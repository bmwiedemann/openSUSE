#
# spec file for package tuxpaint-stamps
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


Name:           tuxpaint-stamps
Version:        2018.09.01
Release:        0
Summary:        Rubber stamps collection for Tux Paint
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
URL:            http://www.tuxpaint.org/
Source0:        %{name}-%{version}.tar.bz2
Requires:       tuxpaint-stamps-category
BuildArch:      noarch
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
Recommends:     tuxpaint
%else
Requires:       tuxpaint
%endif
%if 0%{?suse_version}
Recommends:     tuxpaint-stamps-animals
Recommends:     tuxpaint-stamps-clothes
Recommends:     tuxpaint-stamps-food
Recommends:     tuxpaint-stamps-hobbies
Recommends:     tuxpaint-stamps-household
Recommends:     tuxpaint-stamps-medical
Recommends:     tuxpaint-stamps-military
Recommends:     tuxpaint-stamps-naturalforces
Recommends:     tuxpaint-stamps-people
Recommends:     tuxpaint-stamps-plants
Recommends:     tuxpaint-stamps-seasonal
Recommends:     tuxpaint-stamps-space
Recommends:     tuxpaint-stamps-sports
Recommends:     tuxpaint-stamps-symbols
Recommends:     tuxpaint-stamps-town
Recommends:     tuxpaint-stamps-vehicles
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the documentation for the 'Rubber Stamp' images
which can be used with the "Stamp" tool within Tux Paint.

%package animals
Summary:        Animals stamps stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description animals
tuxpaint-stamps-animals package contains a set of 'Rubber Stamp' images
which can be used with the "Stamp" tool within Tux Paint.

%package clothes
Summary:        Clothes stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description clothes
tuxpaint-stamps-clothes package contains a set of 'Rubber Stamp' images
which can be used with the "Stamp" tool within Tux Paint.

%package food
Summary:        Food stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description food
tuxpaint-stamps-food package contains a set of 'Rubber Stamp' images
which can be used with the "Stamp" tool within Tux Paint.

%package hobbies
Summary:        Hobbies stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description hobbies
tuxpaint-stamps-hobbies package contains a set of 'Rubber Stamp' images
which can be used with the "Stamp" tool within Tux Paint.

%package household
Summary:        Household items stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description household
tuxpaint-stamps-household package contains a set of 'Rubber Stamp' images
which can be used with the "Stamp" tool within Tux Paint.

%package medical
Summary:        Medical stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description medical
tuxpaint-stamps-medical package contains a set of 'Rubber Stamp'
images which can be used with the "Stamp" tool within Tux Paint.

%package military
Summary:        Military stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description military
tuxpaint-stamps-military package contains a set of 'Rubber Stamp'
images which can be used with the "Stamp" tool within Tux Paint.

%package naturalforces
Summary:        Natural forces stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description naturalforces
tuxpaint-stamps-naturalforces package contains a set of 'Rubber Stamp'
images which can be used with the "Stamp" tool within Tux Paint.

%package people
Summary:        People stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description people
tuxpaint-stamps-people package contains a set of 'Rubber Stamp' images
which can be used with the "Stamp" tool within Tux Paint.

%package plants
Summary:        Plants stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description plants
tuxpaint-stamps-plants package contains a set of 'Rubber Stamp' images
which can be used with the "Stamp" tool within Tux Paint.

%package seasonal
Summary:        Seasonal stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description seasonal
tuxpaint-stamps-seasonal package contains a set of 'Rubber Stamp' images
which can be used with the "Stamp" tool within Tux Paint.

%package space
Summary:        Space stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description space
tuxpaint-stamps-space package contains a set of 'Rubber Stamp' images
which can be used with the "Stamp" tool within Tux Paint.

%package sports
Summary:        Sports stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description sports
tuxpaint-stamps-sports package contains a set of 'Rubber Stamp' images
which can be used with the "Stamp" tool within Tux Paint.

%package symbols
Summary:        Symbol stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description symbols
tuxpaint-stamps-symbols package contains a set of 'Rubber Stamp' images
which can be used with the "Stamp" tool within Tux Paint.

%package town
Summary:        Town stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description town
tuxpaint-stamps-town package contains a set of 'Rubber Stamp' images
which can be used with the "Stamp" tool within Tux Paint.

%package vehicles
Summary:        Vehicle stamps collection for Tux Paint
Group:          Productivity/Graphics/Bitmap Editors
Requires:       tuxpaint-stamps
Provides:       tuxpaint-stamps-category = %{version}

%description vehicles
tuxpaint-stamps-vehicles package contains a set of 'Rubber Stamp' images
which can be used with the "Stamp" tool within Tux Paint.

%prep
%setup -q

%build

%install
make DATA_PREFIX=%{buildroot}/%{_datadir}/tuxpaint/ install-all
%if 0%{?suse_version} > 1020
%fdupes %{buildroot}
%endif

%files
%defattr(-,root,root)
%doc docs/*
%dir %{_datadir}/tuxpaint/stamps

%files animals
%defattr(-,root,root)
%{_datadir}/tuxpaint/stamps/animals

%files clothes
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/clothes

%files food
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/food

%files hobbies
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/hobbies

%files household
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/household

%files medical
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/medical

%files military
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/military

%files naturalforces
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/naturalforces

%files people
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/people

%files plants
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/plants

%files seasonal
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/seasonal

%files space
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/space

%files sports
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/sports

%files symbols
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/symbols

%files town
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/town

%files vehicles
%defattr(-,root,root)
%dir %{_datadir}/tuxpaint
%dir %{_datadir}/tuxpaint/stamps
%{_datadir}/tuxpaint/stamps/vehicles

%changelog
