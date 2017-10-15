#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def print_blind_report(report):
    print "SMALL BLIND"
    print "Hands played: {}".format(report.sb_hand_count)
    print "Expected profit: {}".format(report.sb_expected_profit)
    print "Expected VPIP profit: {}".format(report.sb_expected_vpip_profit)
    print "VPIP profit: {}".format(report.sb_vpip_profit)
    print "Expected forced profit: {}".format(report.sb_expected_forced_profit)
    print "Forced profit: {}".format(report.sb_forced_profit)
    print "VPIP%: {}".format(report.sb_vpip * 100)
    print "PFR%: {}".format(report.sb_pfr * 100)
    print "PFR profit: {}".format(report.sb_pfr_profit)
    print "Flat%: {}".format(report.sb_flat * 100)
    print "Flat profit: {}".format(report.sb_flat_profit)
    print "3bet%: {}".format(report.sb_3bet * 100)
    print "3bet profit: {}".format(report.sb_3bet_profit)
    print
    print "BIG BLIND"
    print "Hands played: {}".format(report.bb_hand_count)
    print "Expected profit: {}".format(report.bb_expected_profit)
    print "Expected VPIP profit: {}".format(report.bb_expected_vpip_profit)
    print "VPIP profit: {}".format(report.bb_vpip_profit)
    print "Expected forced profit: {}".format(report.bb_expected_forced_profit)
    print "Forced profit: {}".format(report.bb_forced_profit)
    print "VPIP%: {}".format(report.bb_vpip * 100)
    print "PFR%: {}".format(report.bb_pfr * 100)
    print "PFR profit: {}".format(report.bb_pfr_profit)
    print "Flat%: {}".format(report.bb_flat * 100)
    print "Flat profit: {}".format(report.bb_flat_profit)
    print "3bet%: {}".format(report.bb_3bet * 100)
    print "3bet profit: {}".format(report.bb_3bet_profit)

def print_stats(hands, player):
    for h in []: #hands:
        print(h.lines[0].strip())
        print('PREFLOP')
        print('action {}'.format(reduce(lambda acc, a: acc + str(a) + '|', h.players[player].preflop, "|")))
        print('action {}'.format(reduce(lambda acc, a: acc + str(a) + '|', h.preflop, "|")))

        print('FLOP')
        print('action {}'.format(reduce(lambda acc, a: acc + str(a) + '|', h.players[player].flop, "|")))
        print('action {}'.format(reduce(lambda acc, a: acc + str(a) + '|', h.flop, "|")))

        print('TURN')
        print('action {}'.format(reduce(lambda acc, a: acc + str(a) + '|', h.players[player].turn, "|")))
        print('action {}'.format(reduce(lambda acc, a: acc + str(a) + '|', h.turn, "|")))

        print('RIVER')
        print('action {}'.format(reduce(lambda acc, a: acc + str(a) + '|', h.players[player].river, "|")))
        print('action {}'.format(reduce(lambda acc, a: acc + str(a) + '|', h.river, "|")))

    print('Hand statistics')
    print('Hands: {}'.format(len(hands)))
    positions = ['SB', 'BB', 'UTG', 'MP', 'CO', 'BTN']
    for pos in positions:
        print('{} profit: {}'.format(pos, reduce(lambda acc, h: acc + h.profit_for_player(player), filter(lambda h: h.players[player].position == pos, hands), 0)))
    print('Total profit: {}'.format(reduce(lambda acc, h: acc + h.profit_for_player(player), hands, 0)))
    print('Profit/100: {}'.format(reduce(lambda acc, h: acc + h.profit_for_player(player), hands, 0) * 100 / len(hands)))

    preflop_lines = {}
    flop_lines = {}
    turn_lines = {}
    river_lines = {}
    for h in hands:
        l = reduce(lambda acc, a: acc + a.type.value, h.preflop_actions(player), '')
        preflop_lines[l] = preflop_lines.get(l, 0) + 1
        l = reduce(lambda acc, a: acc + a.type.value, h.flop_actions(player), '')
        flop_lines[l] = flop_lines.get(l, 0) + 1
        l = reduce(lambda acc, a: acc + a.type.value, h.turn_actions(player), '')
        turn_lines[l] = turn_lines.get(l, 0) + 1
        l = reduce(lambda acc, a: acc + a.type.value, h.river_actions(player), '')
        river_lines[l] = river_lines.get(l, 0) + 1

    print('Lines taken (p - post, x - check, c - call, b - bet, r - raise, u - bet uncalled)')
    for (l,c) in preflop_lines.iteritems():
        print('Preflop {}: {}'.format(l, c))
    for (l,c) in flop_lines.iteritems():
        if l != '':
            print('Flop {}: {}'.format(l, c))
    for (l,c) in turn_lines.iteritems():
        if l != '':
            print('Turn {}: {}'.format(l, c))
    for (l,c) in river_lines.iteritems():
        if l != '':
            print('River {}: {}'.format(l, c))