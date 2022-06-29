function mc --description='Midnight Commander'
    set -q TMPDIR || set -gx TMPDIR /tmp
    set -gx _fish_MC_PWD_FILE $TMPDIR/mc-(id -un)/mc.pwd.$fish_pid
    command mc -P "$_fish_MC_PWD_FILE" $argv

    if test -r $_fish_MC_PWD_FILE
        set -gx _fish_MC_PWD (cat $_fish_MC_PWD_FILE)
        if test -n $_fish_MC_PWD && test $_fish_MC_PWD != $PWD && test -d $_fish_MC_PWD
            cd $_fish_MC_PWD
        end
        set -e _fish_MC_PWD
    end

    set -e _fish_MC_PWD_FILE
    set -e _fish_MC_USER

    function _remove_tmp --on-job-exit caller --inherit-variable _fish_MC_PWD_FILE
        command rm $_fish_MC_PWD_FILE
        set -f dirn (dirname $_fish_MC_PWD_FILE)
        if test -d "$dirn"
            rm -f $dirn
        end
        functions -e _remove_tmp
    end
end
