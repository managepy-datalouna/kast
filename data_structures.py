from dataclasses import dataclass
from typing import Optional, List


@dataclass(frozen=True)
class Inventory:
    weapon_name: Optional[str]
    weapon_class: Optional[str]
    ammo_in_magazine: Optional[int]
    ammo_in_reserve: Optional[int]


@dataclass(frozen=True)
class Player:
    steam_id: Optional[int]
    player_name: Optional[str] = None
    name: Optional[str] = None
    team: Optional[str] = None
    side: Optional[str] = None
    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None
    eye_x: Optional[float] = None
    eye_y: Optional[float] = None
    eye_z: Optional[float] = None
    velocity_x: Optional[float] = None
    velocity_y: Optional[float] = None
    velocity_z: Optional[float] = None
    view_x: Optional[float] = None
    view_y: Optional[float] = None
    hp: Optional[int] = None
    armor: Optional[int] = None
    active_weapon: Optional[str] = None
    flash_grenades: Optional[int] = None
    smoke_grenades: Optional[int] = None
    he_grenades: Optional[int] = None
    fire_grenades: Optional[int] = None
    total_utility: Optional[int] = None
    last_place_name: Optional[str] = None
    is_alive: Optional[bool] = None
    is_bot: Optional[bool] = None
    is_blinded: Optional[bool] = None
    is_airborne: Optional[bool] = None
    is_ducking: Optional[bool] = None
    is_ducking_in_progress: Optional[bool] = None
    is_un_ducking_in_progress: Optional[bool] = None
    is_defusing: Optional[bool] = None
    is_planting: Optional[bool] = None
    is_reloading: Optional[bool] = None
    is_in_bomb_zone: Optional[bool] = None
    is_in_buy_zone: Optional[bool] = None
    is_standing: Optional[bool] = None
    is_scoped: Optional[bool] = None
    is_walking: Optional[bool] = None
    is_unknown: Optional[bool] = None
    inventory: Optional[List[Inventory]] = None
    spotters: List[int] = None
    equipment_value: Optional[int] = None
    equipment_value_freezetime_end: Optional[int] = None
    equipment_value_round_start: Optional[int] = None
    cash: Optional[int] = None
    cash_spend_this_round: Optional[int] = None
    cash_spend_total: Optional[int] = None
    has_helmet: Optional[bool] = None
    has_defuse: Optional[bool] = None
    has_bomb: Optional[bool] = None
    ping: Optional[int] = None
    zoom_level: Optional[int] = None


@dataclass(frozen=True)
class Side:
    team_name: Optional[str]
    players: List[Player]
    side: Optional[str] = None
    team_eq_val: Optional[int] = None
    alive_players: Optional[int] = None
    total_utility: Optional[int] = None


@dataclass(frozen=True)
class Kill:
    tick: Optional[int]
    seconds: Optional[float]
    clock_time: Optional[str]
    attacker_steam_id: Optional[int]
    attacker_name: Optional[str]
    attacker_team: Optional[str]
    attacker_side: Optional[str]
    attacker_x: Optional[float]
    attacker_y: Optional[float]
    attacker_z: Optional[float]
    attacker_view_x: Optional[float]
    attacker_view_y: Optional[float]
    victim_steam_id: Optional[int]
    victim_name: Optional[str]
    victim_team: Optional[str]
    victim_side: Optional[str]
    victim_x: Optional[float]
    victim_y: Optional[float]
    victim_z: Optional[float]
    victim_view_x: Optional[float]
    victim_view_y: Optional[float]
    assister_steam_id: Optional[int]
    assister_name: Optional[str]
    assister_team: Optional[str]
    assister_side: Optional[str]
    is_suicide: Optional[bool]
    is_teamkill: Optional[bool]
    is_wallbang: Optional[bool]
    penetrated_objects: Optional[int]
    is_first_kill: Optional[bool]
    is_headshot: Optional[bool]
    victim_blinded: Optional[bool]
    attacker_blinded: Optional[bool]
    flash_thrower_steam_id: Optional[int]
    flash_thrower_name: Optional[str]
    flash_thrower_team: Optional[str]
    flash_thrower_side: Optional[str]
    no_scope: Optional[bool]
    thru_smoke: Optional[bool]
    distance: Optional[float]
    is_trade: Optional[bool]
    player_traded_name: Optional[str]
    player_traded_team: Optional[str]
    player_traded_steam_id: Optional[int]
    weapon: Optional[str]
    weapon_class: Optional[str]


@dataclass(frozen=True)
class Damage:
    tick: Optional[int]
    seconds: Optional[float]
    clock_time: Optional[str]
    attacker_steam_id: Optional[int]
    attacker_name: Optional[str]
    attacker_team: Optional[str]
    attacker_side: Optional[str]
    attacker_x: Optional[float]
    attacker_y: Optional[float]
    attacker_z: Optional[float]
    attacker_view_x: Optional[float]
    attacker_view_y: Optional[float]
    attacker_strafe: Optional[bool]
    victim_steam_id: Optional[int]
    victim_name: Optional[str]
    victim_team: Optional[str]
    victim_side: Optional[str]
    victim_x: Optional[float]
    victim_y: Optional[float]
    victim_z: Optional[float]
    victim_view_x: Optional[float]
    victim_view_y: Optional[float]
    weapon: Optional[str]
    weapon_class: Optional[str]
    hp_damage: Optional[int]
    hp_damage_taken: Optional[int]
    armor_damage: Optional[int]
    armor_damage_taken: Optional[int]
    hit_group: Optional[str]
    is_friendly_fire: Optional[bool]
    distance: Optional[float]
    zoom_level: Optional[int]


@dataclass(frozen=True)
class Grenade:
    throw_tick: Optional[int]
    destroy_tick: Optional[int]
    throw_seconds: Optional[float]
    throw_clock_time: Optional[str]
    destroy_seconds: Optional[float]
    destroy_clock_time: Optional[str]
    thrower_steam_id: Optional[int]
    thrower_name: Optional[str]
    thrower_team: Optional[str]
    thrower_side: Optional[str]
    thrower_x: Optional[float]
    thrower_y: Optional[float]
    thrower_z: Optional[float]
    grenade_type: Optional[str]
    grenade_x: Optional[float]
    grenade_y: Optional[float]
    grenade_z: Optional[float]
    entity_id: Optional[int]


@dataclass(frozen=True)
class WeaponFire:
    tick: Optional[int]
    seconds: Optional[float]
    clock_time: Optional[str]
    player_steam_id: Optional[int]
    player_name: Optional[str]
    player_team: Optional[str]
    player_side: Optional[str]
    player_x: Optional[float]
    player_y: Optional[float]
    player_z: Optional[float]
    player_view_x: Optional[float]
    player_view_y: Optional[float]
    player_strafe: Optional[bool]
    weapon: Optional[str]
    weapon_class: Optional[str]
    ammo_in_magazine: Optional[int]
    ammo_in_reserve: Optional[int]
    zoom_level: Optional[int]


@dataclass(frozen=True)
class Flash:
    tick: Optional[int]
    seconds: Optional[float]
    clock_time: Optional[str]
    attacker_steam_id: Optional[int]
    attacker_name: Optional[str]
    attacker_team: Optional[str]
    attacker_side: Optional[str]
    attacker_x: Optional[float]
    attacker_y: Optional[float]
    attacker_z: Optional[float]
    attacker_view_x: Optional[float]
    attacker_view_y: Optional[float]
    player_steam_id: Optional[int]
    player_name: Optional[str]
    player_team: Optional[str]
    player_side: Optional[str]
    player_x: Optional[float]
    player_y: Optional[float]
    player_z: Optional[float]
    player_view_x: Optional[float]
    player_view_y: Optional[float]
    flash_duration: Optional[float]


@dataclass(frozen=True)
class Bomb:
    x: Optional[float]
    y: Optional[float]
    z: Optional[float]


@dataclass(frozen=True)
class Projectile:
    projectile_type: Optional[str]
    x: Optional[float]
    y: Optional[float]
    z: Optional[float]


@dataclass(frozen=True)
class Smoke:
    grenade_entity_id: Optional[int]
    start_tick: Optional[int]
    x: Optional[float]
    y: Optional[float]
    z: Optional[float]


@dataclass(frozen=True)
class Fire:
    unique_id: Optional[int]
    x: Optional[float]
    y: Optional[float]
    z: Optional[float]


@dataclass(frozen=True)
class Frame:
    is_kill_frame: Optional[bool]
    tick: Optional[int]
    seconds: Optional[float]
    clock_time: Optional[str]
    t: Side
    ct: Side
    bomb_planted: Optional[bool]
    bombsite: Optional[str]
    bomb: Bomb
    projectiles: Optional[List[Projectile]]
    smokes: Optional[List[Smoke]]
    fires: Optional[List[Fire]]


@dataclass(frozen=True)
class BombEvent:
    tick: Optional[int]
    seconds: Optional[float]
    clock_time: Optional[str]
    player_steam_id: Optional[int]
    player_name: Optional[str]
    player_team: Optional[str]
    player_x: Optional[float]
    player_y: Optional[float]
    player_z: Optional[float]
    bomb_action: Optional[str]
    bomb_site: Optional[str]


@dataclass
class GameRound:
    round_num: Optional[int]
    is_warmup: Optional[bool]
    start_tick: Optional[int]
    freeze_time_end_tick: Optional[int]
    end_tick: Optional[int]
    end_official_tick: Optional[int]
    bomb_plant_tick: Optional[int]
    t_score: Optional[int]
    ct_score: Optional[int]
    end_t_score: Optional[int]
    end_ct_score: Optional[int]
    ct_team: Optional[str]
    t_team: Optional[str]
    winning_side: Optional[str]
    winning_team: Optional[str]
    losing_team: Optional[str]
    round_end_reason: Optional[str]
    ct_freeze_time_end_eq_val: Optional[int]
    ct_round_start_eq_val: Optional[int]
    ct_round_spend_money: Optional[int]
    ct_buy_type: Optional[str]
    t_freeze_time_end_eq_val: Optional[int]
    t_round_start_eq_val: Optional[int]
    t_round_spend_money: Optional[int]
    t_buy_type: Optional[str]
    ct_side: Side
    t_side: Side
    kills: List[Kill]
    damages: List[Damage]
    grenades: List[Grenade]
    bomb_events: List[BombEvent]
    weapon_fires: List[WeaponFire]
    flashes: List[Flash]
    frames: List[Frame]
