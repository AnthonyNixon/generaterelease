/**
 * Responds to any HTTP request that can provide a "message" field in the body.
 *
 * @param {!Object} req Cloud Function request context.
 * @param {!Object} res Cloud Function response context.
 */

var animals = {
  'a': 'aardvark',
  'b': 'baboon',
  'c': 'cheetah',
  'd': 'donkey',
  'e': 'elephant',
  'f': 'ferret',
  'g': 'gecko',
  'h': 'hawk',
  'i': 'impala',
  'j': 'jellyfish',
  'k': 'kangaroo',
  'l': 'leopard',
  'm': 'meerkat',
  'n': 'newt',
  'o': 'orangutan',
  'p': 'parrot',
  'q': 'quail',
  'r': 'rabbit',
  's': 'scorpion',
  't': 'toad',
  'u': 'urraca',
  'v': 'viper',
  'w': 'wolf',
  'x': 'xenarthra',
  'y': 'yak',
  'z': 'zebra'
}

exports.helloWorld = function helloWorld(req, res) {
  if (req.query.letter === undefined) {
    // This is an error case, as "message" is required.
    res.status(400).send('No letter defined!');
  } else {
    // Everything is okay.
    console.log(req.query.letter);
    res.status(200).send(animals[req.query.letter]);
  }
};
