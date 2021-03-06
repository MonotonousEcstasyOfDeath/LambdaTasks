const whenDeadline = require('../whenDeadline.js');

test('9 часовый день рабочий день - с утра, до ночи', () => {
  expect(whenDeadline(9, 1654797600000)).toBe(1654876800000);
});
test('У нас заказали ночью. Утром начали, день отработали, на следующий день доделали', () => {
  expect(whenDeadline(10.2, 1654711200000)).toBe(1654848720000);
});
test('Заказали ночью. Утром пятници начали, день отработали, в следующий понедельник доделали', () => {
  expect(whenDeadline(11.2, 1654797600000)).toBe(1655111520000);
});
