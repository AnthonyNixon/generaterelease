/**
 * Responds to any HTTP request that can provide a "message" field in the body.
 *
 * @param {!Object} req Cloud Function request context.
 * @param {!Object} res Cloud Function response context.
 */

const googleapis = require('googleapis');
var request = require('request');

exports.generaterelease = function generaterelease(req, res) {
  if (req.query.letter === undefined) {
    // This is an error case, as "message" is required.
    console.warn(req.query.letter, 'not found');
    res.status(400).send('No letter defined!');
  } else {
    // Everything is okay.

    console.log(req.query.letter);

    var chosenAnimal = ""
    var chosenAdjective = ""

    request.get('https://storage.googleapis.com/adjectives-by-letter/'+req.query.letter.toUpperCase(), function (error, response, body) {
        if (!error && response.statusCode == 200) {
            var adjectiveList = body;
            console.log({"adjectives": adjectiveList})
            // Continue with your processing here.
            var lines = adjectiveList.split('\t');
            console.log(lines)
            chosenAdjective = lines[Math.floor(Math.random()*lines.length)];

            request.get('https://storage.googleapis.com/animals-by-letter/'+req.query.letter.toUpperCase(), function (error, response, body) {
                if (!error && response.statusCode == 200) {
                    var animalList = body;
                    console.log({"animals": animalList})
                    // Continue with your processing here.
                    var lines = animalList.split('\t');
                    console.log(lines)
                    chosenAnimal = lines[Math.floor(Math.random()*lines.length)];
                    res.status(200).send(chosenAdjective + ' ' + chosenAnimal);
                } else {
                  console.error('Problem getting animal file from storage bucket');
                  res.status(500).send('error getting animal file');
                }
            });
        } else {
          console.error('Problem getting adjective file from storage bucket');
          res.status(500).send('error getting adjective file');
        }
    });
  }
};
