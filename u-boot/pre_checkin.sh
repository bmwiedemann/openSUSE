#!/bin/bash -e

if [ ! -e u-boot.spec.tmp ]; then
    # We need to convert u-boot.spec.in into u-boot.spec.tmp first
    /bin/sh update_git.sh
fi

BOARDNAME="$1"
BOARDCONFIG="$2"
ARCH_RESTRICTIONS="$3"

armv6_boards="rpi"

# TI
armv7_boards="omap3_beagle omap4_panda am335x_evm pcm051_rev3 am57xx_evm"
# Exynos
armv7_boards="$armv7_boards arndale snow spring odroid odroid-xu3"
# Calxeda
armv7_boards="$armv7_boards highbank"
# Freescale
armv7_boards="$armv7_boards mx53loco mx6cuboxi mx6qsabrelite udoo udoo_neo"
# Allwinner
armv7_boards="$armv7_boards Bananapi Cubieboard Cubieboard2 Cubietruck Mele_A1000 Merrii_A80_Optimus"
armv7_boards="$armv7_boards A10-OLinuXino-Lime A13-OLinuXino A13-OLinuXinoM"
armv7_boards="$armv7_boards A20-OLinuXino-Lime A20-OLinuXino-Lime2 A20-OLinuXino_MICRO"
armv7_boards="$armv7_boards nanopi_neo nanopi_neo_air orangepi_pc Hyundai_A7HD Lamobo_R1 bananapi_m2_plus_h3"
# Broadcom
armv7_boards="$armv7_boards rpi_2"
# Nvidia
armv7_boards="$armv7_boards colibri_t20 paz00 jetson-tk1"
# Rockchip
armv7_boards="$armv7_boards firefly-rk3288 tinker-rk3288"
# Marvell
armv7_boards="$armv7_boards clearfog turris_omnia"
# Altera
armv7_boards="$armv7_boards socfpga_de0_nano_soc"

aarch64_boards="ls1012afrdm_qspi rpi_3"
# Allwinner
aarch64_boards="$aarch64_boards bananapi_m64 nanopi_a64 orangepi_pc2 pine64_plus pine_h64 pinebook"
# Amlogic
aarch64_boards="$aarch64_boards khadas-vim khadas-vim2 odroid-c2"
# Hisilicon
aarch64_boards="$aarch64_boards hikey poplar"
# Marvell
aarch64_boards="$aarch64_boards mvebu_db-88f3720 mvebu_espressobin-88f3720"
aarch64_boards="$aarch64_boards mvebu_db_armada8k mvebu_mcbin-88f8040"
# Nvidia
aarch64_boards="$aarch64_boards p2371-2180 p2771-0000-500"
# Qualcomm
aarch64_boards="$aarch64_boards dragonboard410c dragonboard820c"
# Rockchip
aarch64_boards="$aarch64_boards geekbox"
aarch64_boards="$aarch64_boards evb-rk3399 firefly-rk3399 rock960-rk3399"
# Xilinx
aarch64_boards="$aarch64_boards xilinx_zynqmp_zcu102_rev1_0 xilinx_zynqmp_generic"

ppc_boards="qemu-ppce500"

riscv64_boards="qemu-riscv64 sifive_fu540"

function generate_spec() {
    sed "s/BOARDCONFIG/$BOARDCONFIG/g
         s/BOARDNAME/$BOARDNAME/g
         s/ARCH_RESTRICTIONS/$ARCH_RESTRICTIONS/g
         s/BINEND/$BINEND/g
         s/ORIGEN_SPL/$ORIGEN_SPL/g
         s/ARNDALE_SPL/$ARNDALE_SPL/g
         s/MVEBU_SPL/$MVEBU_SPL/g
         s/SOCFPGA_SPL/$SOCFPGA_SPL/g
         s/ROCKCHIP_SPL_IMAGE_TYPES/$ROCKCHIP_SPL_IMAGE_TYPES/g
         s/ROCKCHIP_SPL_SOC/$ROCKCHIP_SPL_SOC/g
         s/ROCKCHIP_SPL/$ROCKCHIP_SPL/g
         s/SUNXI_SPL/$SUNXI_SPL/g
         s/TEGRA_SPL/$TEGRA_SPL/g
         s/IMX6_SPL/$IMX6_SPL/g
         s/OMAP_SPL/$OMAP_SPL/g"
}

if [ ! "$1" -o ! "$2" -o ! "$3" ]; then
    # armv6 boards
    for BOARDCONFIG in $armv6_boards; do
        BOARDNAME="$(echo $BOARDCONFIG | tr -d '_' | tr '[:upper:]' '[:lower:]')"
        BOARDCONFIG=${BOARDCONFIG}_defconfig
        ARCH_RESTRICTIONS="armv6l armv6hl"
        bash $0 $BOARDNAME $BOARDCONFIG "$ARCH_RESTRICTIONS"
    done
    # armv7 boards
    for BOARDCONFIG in $armv7_boards; do
        BOARDNAME="$(echo $BOARDCONFIG | tr -d '_' | tr '[:upper:]' '[:lower:]')"
        BOARDCONFIG=${BOARDCONFIG}_defconfig
        ARCH_RESTRICTIONS="armv7l armv7hl"
        bash $0 $BOARDNAME $BOARDCONFIG "$ARCH_RESTRICTIONS"
    done
    # aarch64 boards
    for BOARDCONFIG in $aarch64_boards; do
        BOARDNAME="$(echo $BOARDCONFIG | tr -d '_' | tr '[:upper:]' '[:lower:]')"
        BOARDCONFIG=${BOARDCONFIG}_defconfig
        ARCH_RESTRICTIONS="aarch64"
        bash $0 $BOARDNAME $BOARDCONFIG "$ARCH_RESTRICTIONS"
    done
    # ppc boards
    for BOARDCONFIG in $ppc_boards; do
        BOARDNAME="$(echo $BOARDCONFIG | tr -d '_' | tr '[:upper:]' '[:lower:]')"
        BOARDCONFIG=${BOARDCONFIG}_defconfig
        ARCH_RESTRICTIONS="ppc"
        bash $0 $BOARDNAME $BOARDCONFIG "$ARCH_RESTRICTIONS"
    done
    # riscv64 boards
    for BOARDCONFIG in $riscv64_boards; do
        BOARDNAME="$(echo $BOARDCONFIG | tr -d '_' | tr '[:upper:]' '[:lower:]')"
        BOARDCONFIG=${BOARDCONFIG}_defconfig
        ARCH_RESTRICTIONS="riscv64"
        bash $0 $BOARDNAME $BOARDCONFIG "$ARCH_RESTRICTIONS"
    done

    # Generate u-boot.spec
    generate_spec < u-boot.spec.tmp > u-boot.spec
    exit 0
fi

MVEBU_SPL=0
OMAP_SPL=0
ROCKCHIP_SPL=0
SUNXI_SPL=0
ARNDALE_SPL=0
ORIGEN_SPL=0
IMX6_SPL=0
SOCFPGA_SPL=0
case "$(echo $BOARDCONFIG | sed -e 's/_defconfig//')" in
mx53loco|mx6qsabrelite|efika*)
    BINEND=imx
    ;;
omap*|am335x*|pcm051*)
    BINEND=img
    OMAP_SPL=1
    ;;
arndale)
    BINEND=bin
    ARNDALE_SPL=1
    ;;
Bananapi*|Cubieboard*|Cubietruck*|Hyundai_A7HD|Mele_A1000|nanopi_neo|*-OLinuXino*|orangepi_pc|Lamobo_R1|bananapi_m2_plus_h3)
    BINEND=img
    SUNXI_SPL=1
    ;;
bananapi_m64|nanopi_a64|orangepi_pc2|pine64_plus|pine_h64|pinebook)
    BINEND=itb
    SUNXI_SPL=1
    ;;
snow|spring)
    BINEND=img
    ;;
mx6cuboxi)
    BINEND=img
    IMX6_SPL=1
    ;;
udoo|udoo_neo)
    BINEND=img
    IMX6_SPL=1
    ;;
firefly-rk3288)
    BINEND=bin
    ROCKCHIP_SPL=1
    ROCKCHIP_SPL_IMAGE_TYPES="rksd rkimage"
    ROCKCHIP_SPL_SOC=rk3288
    ;;
tinker-rk3288)
    BINEND=bin
    ROCKCHIP_SPL=1
    ROCKCHIP_SPL_IMAGE_TYPES="rksd"
    ROCKCHIP_SPL_SOC=rk3288
    ;;
evb-rk3399|firefly-rk3399|rock960-rk3399)
    BINEND=bin
    ROCKCHIP_SPL=1
    ROCKCHIP_SPL_IMAGE_TYPES="rksd"
    ROCKCHIP_SPL_SOC=rk3399
    ;;
clearfog|turris_omnia)
    BINEND=img
    MVEBU_SPL=1
    ;;
socfpga_*)
    BINEND=img
    SOCFPGA_SPL=1
    ;;
xilinx*|zynq*)
    BINEND=elf
    ;;

*)  BINEND=bin ;;
esac

generate_spec < u-boot-board.spec.tmp > u-boot-$BOARDNAME.spec

cp u-boot.changes u-boot-$BOARDNAME.changes
