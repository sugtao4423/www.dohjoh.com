// 最終更新日 2019/03/22 00:00:00

// 現在までの総カウント数
var g_total_count   = '00755021';
// 今日のカウント数
var g_today_count   = '00000000';
// 昨日のカウント数
var g_yday_count    = '00000025';

function tkcounter_display(count){
  for(let i = 0; i < count.length; i++){
    const str = `<IMG src="counter/${count.charAt(i)}.gif">`;
    document.write(str);
  }
}