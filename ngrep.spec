Summary:	Networked grep
Summary(pl):	Sieciowy grep
Name:		ngrep
Version:	1.40.1
Release:	1
License:	Freeware
Group:		Applications/Networking
Source0:	http://prdownloads.sf.net/ngrep/%{name}-%{version}.tar.gz
URL:		http://ngrep.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ngrep strives to provide most of GNU grep's common features, applying
them to the network layer. ngrep is a pcap-aware tool that will allow
you to specify extended regular expressions to match against data
payloads of packets. It currently recognizes TCP and UDP across
ethernet, ppp and slip interfaces, and understands bpf filter logic in
the same fashion as more common packet sniffing tools, like tcpdump
and snoop.

%description -l pl
Ngrep próbuje wype³niæ zadania stawiane grep-owi, w odniesieniu do
poziomu sieci. Ngrep korzysta z biblioteki pcap, pozwala na
korzystanie z wyra¿eñ regularnych zastosowanych do pakietów czy
kawa³ków danych. Obecnie obrabia pakiety TCP i UDP przychodz±ce na
interfejsy ethernet, ppp i slip. Ngrep zna zasady filtrowania bpf w
takim samym stylu jak czê¶ciej u¿ywane pakiety typu tpcdump czy snoop.

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install ngrep $RPM_BUILD_ROOT%{_sbindir}
install ngrep.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README COPYRIGHT
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
