Name:           cozy
Version:        0.6.11
Release:        1
Summary:        Audio Book Player
License:        GPL-3
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/geigi
Source0:        https://github.com/geigi/cozy/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python-setuptools
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       python3dist(pycairo)
Requires:       python3dist(distro)
Requires:       python-gstreamer1.0
Requires:       python3dist(file-magic)
# Need to import it 3x
Requires:       python3-mutagen
Requires:       python3-peewee
Requires:       python3-pytaglib

Recommends:     %{name}-lang
Recommends:     gstreamer1.0-plugins-base
Recommends:     gstreamer1.0-plugins-bad
Recommends:     gstreamer1.0-plugins-ugly
Conflicts:      com.github.geigi.cozy
Provides:       com.github.geigi.cozy = %{version}
BuildArch:      noarch

# Needed for tests
BuildRequires:  pkgconfig(py3cairo)
BuildRequires:  python-gstreamer1.0
BuildRequires:  python3dist(file-magic)
#Need import 3x
BuildRequires:  python3-mutagen
BuildRequires:  python3-peewee
BuildRequires:  python3-pytaglib

BuildRequires:  python3dist(distro)


%description
Play and organize your audio book collection.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang com.github.geigi.cozy %{name}.lang
%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{python_sitelib}

%files
%defattr(0644,root,root,0755)
%license COPYING
%doc AUTHORS README.md
%attr(0755,root,root) %{_bindir}/com.github.geigi.cozy
%{_datadir}/applications/com.github.geigi.cozy.desktop
%{_datadir}/glib-2.0/schemas/com.github.geigi.cozy.gschema.xml
%{_datadir}/metainfo/com.github.geigi.cozy.appdata.xml
%{_datadir}/icons/hicolor/*/*/*.??g
%{_datadir}/com.github.geigi.cozy/
%{python_sitelib}/cozy/

%files lang -f %{name}.lang
