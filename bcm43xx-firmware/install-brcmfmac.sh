#!/bin/sh

if [[ -e /sys/firmware/devicetree/base/compatible ]]; then
  while IFS= read -r -d '' compatible; do
    case "$compatible" in
    sinovoip,bpi-m2)
      ln -sf brcmfmac43362-sdio-bananapi-m2.txt /lib/firmware/brcm/brcmfmac43362-sdio.txt
      ;;
    cubietech,cubietruck)
      ln -sf brcmfmac43362-sdio-cubietruck.txt /lib/firmware/brcm/brcmfmac43362-sdio.txt
      ;;
    solidrun,cubox-i)
      ln -sf brcmfmac4329-sdio-cubox-i.txt /lib/firmware/brcm/brcmfmac4329-sdio.txt
      ln -sf brcmfmac4330-sdio-cubox-i.txt /lib/firmware/brcm/brcmfmac4330-sdio.txt
      ;;
    tronsmart,vega-s95-telos)
      ln -sf brcmfmac4339-sdio-vega-s95-telos.txt /lib/firmware/brcm/brcmfmac4339-sdio.txt
      ;;
    esac
  done < /sys/firmware/devicetree/base/compatible
fi

/usr/sbin/modprobe --ignore-install brcmfmac "$@" || exit $?

exit 0
