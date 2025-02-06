#
# spec file for package perl-DateTime-TimeZone
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


%define cpan_name DateTime-TimeZone
Name:           perl-DateTime-TimeZone
Version:        2.640.0
Release:        0
# 2.64 -> normalize -> 2.640.0
%define cpan_version 2.64
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Time zone object base class and factory
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Singleton) >= 1.03
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Params::ValidationCompiler) >= 0.13
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
Requires:       perl(Class::Singleton) >= 1.03
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Module::Runtime)
Requires:       perl(Params::ValidationCompiler) >= 0.13
Requires:       perl(Specio::Library::Builtins)
Requires:       perl(Specio::Library::String)
Requires:       perl(Try::Tiny)
Requires:       perl(namespace::autoclean)
Requires:       perl(parent)
Provides:       perl(DateTime::TimeZone) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Abidjan) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Algiers) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Bissau) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Cairo) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Casablanca) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Ceuta) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::El_Aaiun) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Johannesburg) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Juba) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Khartoum) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Lagos) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Maputo) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Monrovia) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Nairobi) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Ndjamena) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Sao_Tome) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Tripoli) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Tunis) = %{version}
Provides:       perl(DateTime::TimeZone::Africa::Windhoek) = %{version}
Provides:       perl(DateTime::TimeZone::America::Adak) = %{version}
Provides:       perl(DateTime::TimeZone::America::Anchorage) = %{version}
Provides:       perl(DateTime::TimeZone::America::Araguaina) = %{version}
Provides:       perl(DateTime::TimeZone::America::Argentina::Buenos_Aires) = %{version}
Provides:       perl(DateTime::TimeZone::America::Argentina::Catamarca) = %{version}
Provides:       perl(DateTime::TimeZone::America::Argentina::Cordoba) = %{version}
Provides:       perl(DateTime::TimeZone::America::Argentina::Jujuy) = %{version}
Provides:       perl(DateTime::TimeZone::America::Argentina::La_Rioja) = %{version}
Provides:       perl(DateTime::TimeZone::America::Argentina::Mendoza) = %{version}
Provides:       perl(DateTime::TimeZone::America::Argentina::Rio_Gallegos) = %{version}
Provides:       perl(DateTime::TimeZone::America::Argentina::Salta) = %{version}
Provides:       perl(DateTime::TimeZone::America::Argentina::San_Juan) = %{version}
Provides:       perl(DateTime::TimeZone::America::Argentina::San_Luis) = %{version}
Provides:       perl(DateTime::TimeZone::America::Argentina::Tucuman) = %{version}
Provides:       perl(DateTime::TimeZone::America::Argentina::Ushuaia) = %{version}
Provides:       perl(DateTime::TimeZone::America::Asuncion) = %{version}
Provides:       perl(DateTime::TimeZone::America::Bahia) = %{version}
Provides:       perl(DateTime::TimeZone::America::Bahia_Banderas) = %{version}
Provides:       perl(DateTime::TimeZone::America::Barbados) = %{version}
Provides:       perl(DateTime::TimeZone::America::Belem) = %{version}
Provides:       perl(DateTime::TimeZone::America::Belize) = %{version}
Provides:       perl(DateTime::TimeZone::America::Boa_Vista) = %{version}
Provides:       perl(DateTime::TimeZone::America::Bogota) = %{version}
Provides:       perl(DateTime::TimeZone::America::Boise) = %{version}
Provides:       perl(DateTime::TimeZone::America::Cambridge_Bay) = %{version}
Provides:       perl(DateTime::TimeZone::America::Campo_Grande) = %{version}
Provides:       perl(DateTime::TimeZone::America::Cancun) = %{version}
Provides:       perl(DateTime::TimeZone::America::Caracas) = %{version}
Provides:       perl(DateTime::TimeZone::America::Cayenne) = %{version}
Provides:       perl(DateTime::TimeZone::America::Chicago) = %{version}
Provides:       perl(DateTime::TimeZone::America::Chihuahua) = %{version}
Provides:       perl(DateTime::TimeZone::America::Ciudad_Juarez) = %{version}
Provides:       perl(DateTime::TimeZone::America::Costa_Rica) = %{version}
Provides:       perl(DateTime::TimeZone::America::Cuiaba) = %{version}
Provides:       perl(DateTime::TimeZone::America::Danmarkshavn) = %{version}
Provides:       perl(DateTime::TimeZone::America::Dawson) = %{version}
Provides:       perl(DateTime::TimeZone::America::Dawson_Creek) = %{version}
Provides:       perl(DateTime::TimeZone::America::Denver) = %{version}
Provides:       perl(DateTime::TimeZone::America::Detroit) = %{version}
Provides:       perl(DateTime::TimeZone::America::Edmonton) = %{version}
Provides:       perl(DateTime::TimeZone::America::Eirunepe) = %{version}
Provides:       perl(DateTime::TimeZone::America::El_Salvador) = %{version}
Provides:       perl(DateTime::TimeZone::America::Fort_Nelson) = %{version}
Provides:       perl(DateTime::TimeZone::America::Fortaleza) = %{version}
Provides:       perl(DateTime::TimeZone::America::Glace_Bay) = %{version}
Provides:       perl(DateTime::TimeZone::America::Goose_Bay) = %{version}
Provides:       perl(DateTime::TimeZone::America::Grand_Turk) = %{version}
Provides:       perl(DateTime::TimeZone::America::Guatemala) = %{version}
Provides:       perl(DateTime::TimeZone::America::Guayaquil) = %{version}
Provides:       perl(DateTime::TimeZone::America::Guyana) = %{version}
Provides:       perl(DateTime::TimeZone::America::Halifax) = %{version}
Provides:       perl(DateTime::TimeZone::America::Havana) = %{version}
Provides:       perl(DateTime::TimeZone::America::Hermosillo) = %{version}
Provides:       perl(DateTime::TimeZone::America::Indiana::Indianapolis) = %{version}
Provides:       perl(DateTime::TimeZone::America::Indiana::Knox) = %{version}
Provides:       perl(DateTime::TimeZone::America::Indiana::Marengo) = %{version}
Provides:       perl(DateTime::TimeZone::America::Indiana::Petersburg) = %{version}
Provides:       perl(DateTime::TimeZone::America::Indiana::Tell_City) = %{version}
Provides:       perl(DateTime::TimeZone::America::Indiana::Vevay) = %{version}
Provides:       perl(DateTime::TimeZone::America::Indiana::Vincennes) = %{version}
Provides:       perl(DateTime::TimeZone::America::Indiana::Winamac) = %{version}
Provides:       perl(DateTime::TimeZone::America::Inuvik) = %{version}
Provides:       perl(DateTime::TimeZone::America::Iqaluit) = %{version}
Provides:       perl(DateTime::TimeZone::America::Jamaica) = %{version}
Provides:       perl(DateTime::TimeZone::America::Juneau) = %{version}
Provides:       perl(DateTime::TimeZone::America::Kentucky::Louisville) = %{version}
Provides:       perl(DateTime::TimeZone::America::Kentucky::Monticello) = %{version}
Provides:       perl(DateTime::TimeZone::America::La_Paz) = %{version}
Provides:       perl(DateTime::TimeZone::America::Lima) = %{version}
Provides:       perl(DateTime::TimeZone::America::Los_Angeles) = %{version}
Provides:       perl(DateTime::TimeZone::America::Maceio) = %{version}
Provides:       perl(DateTime::TimeZone::America::Managua) = %{version}
Provides:       perl(DateTime::TimeZone::America::Manaus) = %{version}
Provides:       perl(DateTime::TimeZone::America::Martinique) = %{version}
Provides:       perl(DateTime::TimeZone::America::Matamoros) = %{version}
Provides:       perl(DateTime::TimeZone::America::Mazatlan) = %{version}
Provides:       perl(DateTime::TimeZone::America::Menominee) = %{version}
Provides:       perl(DateTime::TimeZone::America::Merida) = %{version}
Provides:       perl(DateTime::TimeZone::America::Metlakatla) = %{version}
Provides:       perl(DateTime::TimeZone::America::Mexico_City) = %{version}
Provides:       perl(DateTime::TimeZone::America::Miquelon) = %{version}
Provides:       perl(DateTime::TimeZone::America::Moncton) = %{version}
Provides:       perl(DateTime::TimeZone::America::Monterrey) = %{version}
Provides:       perl(DateTime::TimeZone::America::Montevideo) = %{version}
Provides:       perl(DateTime::TimeZone::America::New_York) = %{version}
Provides:       perl(DateTime::TimeZone::America::Nome) = %{version}
Provides:       perl(DateTime::TimeZone::America::Noronha) = %{version}
Provides:       perl(DateTime::TimeZone::America::North_Dakota::Beulah) = %{version}
Provides:       perl(DateTime::TimeZone::America::North_Dakota::Center) = %{version}
Provides:       perl(DateTime::TimeZone::America::North_Dakota::New_Salem) = %{version}
Provides:       perl(DateTime::TimeZone::America::Nuuk) = %{version}
Provides:       perl(DateTime::TimeZone::America::Ojinaga) = %{version}
Provides:       perl(DateTime::TimeZone::America::Panama) = %{version}
Provides:       perl(DateTime::TimeZone::America::Paramaribo) = %{version}
Provides:       perl(DateTime::TimeZone::America::Phoenix) = %{version}
Provides:       perl(DateTime::TimeZone::America::Port_au_Prince) = %{version}
Provides:       perl(DateTime::TimeZone::America::Porto_Velho) = %{version}
Provides:       perl(DateTime::TimeZone::America::Puerto_Rico) = %{version}
Provides:       perl(DateTime::TimeZone::America::Punta_Arenas) = %{version}
Provides:       perl(DateTime::TimeZone::America::Rankin_Inlet) = %{version}
Provides:       perl(DateTime::TimeZone::America::Recife) = %{version}
Provides:       perl(DateTime::TimeZone::America::Regina) = %{version}
Provides:       perl(DateTime::TimeZone::America::Resolute) = %{version}
Provides:       perl(DateTime::TimeZone::America::Rio_Branco) = %{version}
Provides:       perl(DateTime::TimeZone::America::Santarem) = %{version}
Provides:       perl(DateTime::TimeZone::America::Santiago) = %{version}
Provides:       perl(DateTime::TimeZone::America::Santo_Domingo) = %{version}
Provides:       perl(DateTime::TimeZone::America::Sao_Paulo) = %{version}
Provides:       perl(DateTime::TimeZone::America::Scoresbysund) = %{version}
Provides:       perl(DateTime::TimeZone::America::Sitka) = %{version}
Provides:       perl(DateTime::TimeZone::America::St_Johns) = %{version}
Provides:       perl(DateTime::TimeZone::America::Swift_Current) = %{version}
Provides:       perl(DateTime::TimeZone::America::Tegucigalpa) = %{version}
Provides:       perl(DateTime::TimeZone::America::Thule) = %{version}
Provides:       perl(DateTime::TimeZone::America::Tijuana) = %{version}
Provides:       perl(DateTime::TimeZone::America::Toronto) = %{version}
Provides:       perl(DateTime::TimeZone::America::Vancouver) = %{version}
Provides:       perl(DateTime::TimeZone::America::Whitehorse) = %{version}
Provides:       perl(DateTime::TimeZone::America::Winnipeg) = %{version}
Provides:       perl(DateTime::TimeZone::America::Yakutat) = %{version}
Provides:       perl(DateTime::TimeZone::Antarctica::Casey) = %{version}
Provides:       perl(DateTime::TimeZone::Antarctica::Davis) = %{version}
Provides:       perl(DateTime::TimeZone::Antarctica::Macquarie) = %{version}
Provides:       perl(DateTime::TimeZone::Antarctica::Mawson) = %{version}
Provides:       perl(DateTime::TimeZone::Antarctica::Palmer) = %{version}
Provides:       perl(DateTime::TimeZone::Antarctica::Rothera) = %{version}
Provides:       perl(DateTime::TimeZone::Antarctica::Troll) = %{version}
Provides:       perl(DateTime::TimeZone::Antarctica::Vostok) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Almaty) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Amman) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Anadyr) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Aqtau) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Aqtobe) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Ashgabat) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Atyrau) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Baghdad) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Baku) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Bangkok) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Barnaul) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Beirut) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Bishkek) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Chita) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Colombo) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Damascus) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Dhaka) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Dili) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Dubai) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Dushanbe) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Famagusta) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Gaza) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Hebron) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Ho_Chi_Minh) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Hong_Kong) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Hovd) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Irkutsk) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Jakarta) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Jayapura) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Jerusalem) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Kabul) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Kamchatka) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Karachi) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Kathmandu) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Khandyga) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Kolkata) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Krasnoyarsk) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Kuching) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Macau) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Magadan) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Makassar) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Manila) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Nicosia) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Novokuznetsk) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Novosibirsk) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Omsk) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Oral) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Pontianak) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Pyongyang) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Qatar) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Qostanay) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Qyzylorda) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Riyadh) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Sakhalin) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Samarkand) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Seoul) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Shanghai) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Singapore) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Srednekolymsk) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Taipei) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Tashkent) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Tbilisi) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Tehran) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Thimphu) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Tokyo) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Tomsk) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Ulaanbaatar) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Urumqi) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Ust_Nera) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Vladivostok) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Yakutsk) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Yangon) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Yekaterinburg) = %{version}
Provides:       perl(DateTime::TimeZone::Asia::Yerevan) = %{version}
Provides:       perl(DateTime::TimeZone::Atlantic::Azores) = %{version}
Provides:       perl(DateTime::TimeZone::Atlantic::Bermuda) = %{version}
Provides:       perl(DateTime::TimeZone::Atlantic::Canary) = %{version}
Provides:       perl(DateTime::TimeZone::Atlantic::Cape_Verde) = %{version}
Provides:       perl(DateTime::TimeZone::Atlantic::Faroe) = %{version}
Provides:       perl(DateTime::TimeZone::Atlantic::Madeira) = %{version}
Provides:       perl(DateTime::TimeZone::Atlantic::South_Georgia) = %{version}
Provides:       perl(DateTime::TimeZone::Atlantic::Stanley) = %{version}
Provides:       perl(DateTime::TimeZone::Australia::Adelaide) = %{version}
Provides:       perl(DateTime::TimeZone::Australia::Brisbane) = %{version}
Provides:       perl(DateTime::TimeZone::Australia::Broken_Hill) = %{version}
Provides:       perl(DateTime::TimeZone::Australia::Darwin) = %{version}
Provides:       perl(DateTime::TimeZone::Australia::Eucla) = %{version}
Provides:       perl(DateTime::TimeZone::Australia::Hobart) = %{version}
Provides:       perl(DateTime::TimeZone::Australia::Lindeman) = %{version}
Provides:       perl(DateTime::TimeZone::Australia::Lord_Howe) = %{version}
Provides:       perl(DateTime::TimeZone::Australia::Melbourne) = %{version}
Provides:       perl(DateTime::TimeZone::Australia::Perth) = %{version}
Provides:       perl(DateTime::TimeZone::Australia::Sydney) = %{version}
Provides:       perl(DateTime::TimeZone::Catalog) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Andorra) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Astrakhan) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Athens) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Belgrade) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Berlin) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Brussels) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Bucharest) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Budapest) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Chisinau) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Dublin) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Gibraltar) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Helsinki) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Istanbul) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Kaliningrad) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Kirov) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Kyiv) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Lisbon) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::London) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Madrid) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Malta) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Minsk) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Moscow) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Paris) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Prague) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Riga) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Rome) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Samara) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Saratov) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Simferopol) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Sofia) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Tallinn) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Tirane) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Ulyanovsk) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Vienna) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Vilnius) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Volgograd) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Warsaw) = %{version}
Provides:       perl(DateTime::TimeZone::Europe::Zurich) = %{version}
Provides:       perl(DateTime::TimeZone::Floating) = %{version}
Provides:       perl(DateTime::TimeZone::Indian::Chagos) = %{version}
Provides:       perl(DateTime::TimeZone::Indian::Maldives) = %{version}
Provides:       perl(DateTime::TimeZone::Indian::Mauritius) = %{version}
Provides:       perl(DateTime::TimeZone::Local) = %{version}
Provides:       perl(DateTime::TimeZone::Local::Android) = %{version}
Provides:       perl(DateTime::TimeZone::Local::Unix) = %{version}
Provides:       perl(DateTime::TimeZone::Local::VMS) = %{version}
Provides:       perl(DateTime::TimeZone::OffsetOnly) = %{version}
Provides:       perl(DateTime::TimeZone::OlsonDB) = %{version}
Provides:       perl(DateTime::TimeZone::OlsonDB::Change) = %{version}
Provides:       perl(DateTime::TimeZone::OlsonDB::Observance) = %{version}
Provides:       perl(DateTime::TimeZone::OlsonDB::Rule) = %{version}
Provides:       perl(DateTime::TimeZone::OlsonDB::Zone) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Apia) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Auckland) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Bougainville) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Chatham) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Easter) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Efate) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Fakaofo) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Fiji) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Galapagos) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Gambier) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Guadalcanal) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Guam) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Honolulu) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Kanton) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Kiritimati) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Kosrae) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Kwajalein) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Marquesas) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Nauru) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Niue) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Norfolk) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Noumea) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Pago_Pago) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Palau) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Pitcairn) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Port_Moresby) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Rarotonga) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Tahiti) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Tarawa) = %{version}
Provides:       perl(DateTime::TimeZone::Pacific::Tongatapu) = %{version}
Provides:       perl(DateTime::TimeZone::UTC) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This class is the base class for all time zone objects. A time zone is
represented internally as a set of observances, each of which describes the
offset from GMT for a given time period.

Note that without the DateTime module, this module does not do much. It's
primary interface is through a DateTime object, and most users will not
need to directly use 'DateTime::TimeZone' methods.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
