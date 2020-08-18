#coding: utf-8
import ipaddress

def main(): 

    # IPアドレス一覧ファイルをリストに読み込み
    with open('./iplist.txt') as f_ip:
        list_ip = f_ip.readlines()

    # ネットワークアドレス一覧ファイルをリストに読み込み
    with open('./netlist.txt') as f_net:
        list_net = f_net.readlines()

    # IPアドレスリストでループ
    for ipaddr in list_ip:
        # 改行コードを削除（IPアドレス一覧）
        ipaddr = ipaddr.strip()

        # 判定フラグを初期化
        flag_match = False

        # ネットワークアドレスリストでループ
        for netaddr in list_net:
            # 改行コードを削除（ネットワークアドレス一覧）
            netaddr = netaddr.strip()

            # 判定
            if ipaddress.ip_address(ipaddr) in ipaddress.ip_network(netaddr):
                # IPアドレスがネットワークアドレスに含まれるとき
                # 判定フラグをTrueにする
                flag_match = True
                # マッチしたネットワークアドレスを for の外でも正しく使えるよう別変数にセット
                match_netaddr = netaddr
                # for ループを抜ける
                continue

        if flag_match:
            # 含まれたとき
            print('あるときー: ' + ipaddr + ' -> ' + match_netaddr)
        else:
            # 含まれないとき
            print('ないときー: ' + ipaddr)


if __name__ == '__main__':
    main()
