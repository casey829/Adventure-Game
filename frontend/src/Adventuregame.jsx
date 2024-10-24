import { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Moon, Sun, House, Tree, Flashlight, Treasure, Ghost, Cave } from 'lucide-react';

const API_URL = 'http://localhost:8000';

function AdventureGame () {
  const [gameState, setGameState] = useState({
    currentScene: 'loading',
    message: 'Loading game...',
    choices: [],
    gameOver: false
  });

  const [loading, setLoading] = useState(false);

  useEffect(() => {
    startGame();
  }, []);

  const startGame = async () => {
    try {
      const response = await fetch(`${API_URL}/start`);
      const data = await response.json();
      setGameState(data);
    } catch (error) {
      console.error('Error starting game:', error);
      setGameState({
        currentScene: 'error',
        message: 'Failed to start game. Please try again.',
        choices: [{ text: 'Retry', value: 'restart' }],
        gameOver: true
      });
    }
  };

  const handleChoice = async (choice) => {
    if (choice === 'restart') {
      return startGame();
    }

    setLoading(true);
    try {
      const response = await fetch(`${API_URL}/make_choice`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          scene: gameState.currentScene,
          choice: choice
        }),
      });
      
      const data = await response.json();
      setGameState(data);
    } catch (error) {
      console.error('Error making choice:', error);
      setGameState({
        currentScene: 'error',
        message: 'Something went wrong. Please try again.',
        choices: [{ text: 'Restart', value: 'restart' }],
        gameOver: true
      });
    } finally {
      setLoading(false);
    }
  };

  const getSceneIcon = () => {
    switch (gameState.currentScene) {
      case 'start':
        return <Tree className="w-12 h-12 text-green-600" />;
      case 'house':
        return <House className="w-12 h-12 text-gray-600" />;
      case 'basement':
        return <Flashlight className="w-12 h-12 text-yellow-500" />;
      case 'cave':
        return <Cave className="w-12 h-12 text-gray-700" />;
      case 'win':
        return <Treasure className="w-12 h-12 text-yellow-500" />;
      case 'lose':
        return <Ghost className="w-12 h-12 text-gray-400" />;
      default:
        return <Moon className="w-12 h-12 text-blue-600" />;
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 flex items-center justify-center p-4">
      <Card className="w-full max-w-2xl bg-gray-800 text-white">
        <CardHeader className="text-center border-b border-gray-700">
          <CardTitle className="text-3xl font-bold flex items-center justify-center gap-4">
            <Sun className="w-8 h-8 text-yellow-500" />
            Adventure Game
            <Moon className="w-8 h-8 text-blue-500" />
          </CardTitle>
        </CardHeader>
        <CardContent className="p-6">
          <div className="flex flex-col items-center gap-6">
            <div className="p-4 rounded-full bg-gray-700">
              {getSceneIcon()}
            </div>
            
            <p className="text-lg text-center mb-6">
              {gameState.message}
            </p>

            <div className="flex flex-col gap-4 w-full max-w-md">
              {gameState.choices.map((choice, index) => (
                <Button
                  key={index}
                  onClick={() => handleChoice(choice.value)}
                  disabled={loading}
                  className="w-full py-6 text-lg bg-blue-600 hover:bg-blue-700 disabled:opacity-50"
                >
                  {choice.text}
                </Button>
              ))}
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default AdventureGame;